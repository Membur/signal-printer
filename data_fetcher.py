import os
import yfinance as yf
import pandas as pd  # Import pandas for reading CSV

# Define the directory to save the data
data_dir = 'data'  # Change this to your desired directory

# Read the list of stock symbols from the CSV file
symbols_csv_path = 'tools/symbols.csv'  # Adjust the path as needed
symbols_df = pd.read_csv(symbols_csv_path)
symbols = symbols_df['ticker'].tolist()  # Assuming the CSV has a 'Symbol' column

# Create the data directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)

# Fetch data for each symbol and save it to a CSV file
for symbol in symbols:
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        data.to_csv(os.path.join(data_dir, f'{symbol}_data.csv'))
        print(f'Data for {symbol} saved to {data_dir}/{symbol}_data.csv')
    except Exception as e:
        print(f'Failed to fetch data for {symbol}: {e}')
