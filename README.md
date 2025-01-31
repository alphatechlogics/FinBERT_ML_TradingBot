# FinBERT Sentiment-Based Alpaca Trading Bot

This project implements a sentiment-based trading bot using the Alpaca API for trading and the FinBERT model for sentiment analysis. The bot trades based on the sentiment of recent news headlines related to a specified stock symbol.

## Table of Contents

- **[Features](#features)**
- **[Installation](#installation)**
- **[Usage](#usage)**
- **[Files](#files)**

## Features

- **Alpaca Integration:** Uses the Alpaca API to place buy/sell orders and manage positions.
- **Sentiment Analysis:** Leverages the FinBERT model (a pre-trained BERT model) to predict the sentiment of financial news headlines.
- **Backtesting:** Includes the ability to backtest the strategy with historical data using Yahoo Finance.
- **Risk Management:** Implements stop-loss and take-profit mechanisms for automated trade execution.

## Installation

1. Clone the repository:

```bash
git https://github.com/alphatechlogics/FinBERT_ML_TradingBot.git
cd FinBERT_ML_TradingBot
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Set up environment variables: Create a .env file in the root directory and add your Alpaca API credentials:

```
API_KEY=your_alpaca_api_key
API_SECRET=your_alpaca_api_secret
BASE_URL=https://paper-api.alpaca.markets
```

## Usage

1. Run the trading bot:

```bash
python tradingbot.py
```

2. Backtest the strategy: The backtesting is already included in the tradingbot.py script. It uses Yahoo Finance data to backtest the strategy from January 1, 2020, to January 1, 2025.

## Files

- **tradingbot.py**: Contains the main trading bot implementation.
- **finbert_utils.py**: Contains the sentiment analysis function using the FinBERT model.
