import os
import talib
import yfinance as yf
import pandas as pd
import csv

# Define candlestick patterns to detect
candlestick_patterns = {
    'CDL2CROWS':'Two Crows',
    'CDL3BLACKCROWS':'Three Black Crows',
    # Add more candlestick patterns as needed
}

# Function to detect candlestick patterns for a given symbol
def detect_candlestick_patterns(symbol, data_dir):
    pattern_results = {}
    
    # Load historical price data
    data_file = os.path.join(data_dir, '1wk-data', f'{symbol}_data.csv')
    if not os.path.exists(data_file):
        print(f"Data file for {symbol} not found. Skipping...")
        return pattern_results
    
    data = pd.read_csv(data_file, index_col=0)
    
    for pattern_code, pattern_name in candlestick_patterns.items():
        try:
            pattern_function = getattr(talib, pattern_code)
            pattern_results[pattern_name] = pattern_function(data['Open'], data['High'], data['Low'], data['Close']).iloc[-1]
        except Exception as e:
            print(f"Failed to detect {pattern_name} for {symbol}: {e}")
            pattern_results[pattern_name] = None
    
    return pattern_results

# Add this function to your existing code to detect and print candlestick patterns for each symbol
def detect_and_print_candlestick_patterns(data_dir):
    with open('tools/symbols.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            
            pattern_results = detect_candlestick_patterns(symbol, data_dir)
            
            print(f"Candlestick Patterns for {symbol}:")
            for pattern, result in pattern_results.items():
                if result > 0:
                    print(f"{pattern}: Bullish")
                elif result < 0:
                    print(f"{pattern}: Bearish")
                else:
                    print(f"{pattern}: No signal")

if __name__ == "__main__":
    data_dir = 'C:/Users/Sean/Documents/Python Scripts/signal-printer/patterns'
    detect_and_print_candlestick_patterns(data_dir)
