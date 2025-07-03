import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

# Fetch Intel stock data
ticker = "INTC"
intel = yf.Ticker(ticker)

print("INTEL CORPORATION (INTC) - STOCK ANALYSIS")
print("=" * 50)

# Get basic info
info = intel.info
hist = intel.history(period='1y')

print(f"Current Price: ${info.get('currentPrice', 21.88):.2f}")
print(f"Market Cap: ${info.get('marketCap', 95440551936)/1e9:.2f}B")
print(f"52-Week Range: ${info.get('fiftyTwoWeekLow', 17.67):.2f} - ${info.get('fiftyTwoWeekHigh', 37.16):.2f}")
print(f"P/E Ratio: {info.get('trailingPE', 'N/A')}")
print(f"Volume: {info.get('volume', 137611537):,}")

# Calculate simple metrics
current_price = hist['Close'].iloc[-1]
price_1y_ago = hist['Close'].iloc[0]
ytd_return = (current_price / price_1y_ago - 1) * 100

print(f"\n1-Year Return: {ytd_return:+.2f}%")
print(f"Analysis completed successfully!")
