import yfinance as yf

def load_data_yf(symbol, start_date, end_date):
    """
    Load historical stock data from Yahoo Finance.

    Args:
        symbol (str): The stock symbol (e.g., AAPL for Apple Inc.).
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: A DataFrame containing historical stock data.
    """
    try:
        data = yf.download(symbol, start=start_date, end=end_date, interval="1wk")
        return data
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")
        return None
    