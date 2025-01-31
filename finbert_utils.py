from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

tokenizer = AutoTokenizer.from_pretrained('ProsusAI/finbert')
model = AutoModelForSequenceClassification.from_pretrained(
    'ProsusAI/finbert').to(device)
labels = ['positive', 'negative', 'neutral']


def predict_sentiment(news) -> str:
    if news:
        tokens = tokenizer(news, return_tensors='pt', padding=True).to(device)
        logits = model(tokens['input_ids'], attention_mask=tokens['attention_mask'])[
            'logits']
        predictions = torch.argmax(logits, dim=-1)
        labels_pred = [labels[pred] for pred in predictions.cpu().numpy()]
        # Aggregate sentiments, e.g., by majority vote
        sentiment = max(set(labels_pred), key=labels_pred.count)
        return sentiment
    else:
        return 'neutral'
