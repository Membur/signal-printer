import talib

def calculate_rsi(data):
    """
    Calculate the Relative Strength Index (RSI) for the given data.

    Args:
        data (pandas.DataFrame): DataFrame containing 'Close' prices.

    Returns:
        pandas.Series: RSI values.
    """
    return talib.RSI(data['Close'])

def calculate_macd(data):
    """
    Calculate the Moving Average Convergence Divergence (MACD) for the given data.

    Args:
        data (pandas.DataFrame): DataFrame containing 'Close' prices.

    Returns:
        pandas.Series: MACD values.
    """
    macd, _, _ = talib.MACD(data['Close'])
    return macd

def calculate_stochastic(data):
    """
    Calculate the Stochastic Oscillator (K and D) for the given data.

    Args:
        data (pandas.DataFrame): DataFrame containing 'High', 'Low', and 'Close' prices.

    Returns:
        tuple: Two pandas.Series, representing K and D values.
    """
    k, d = talib.STOCH(data['High'], data['Low'], data['Close'])
    return k, d

def calculate_cci(data):
    """
    Calculate the Commodity Channel Index (CCI) for the given data.

    Args:
        data (pandas.DataFrame): DataFrame containing 'High', 'Low', and 'Close' prices.

    Returns:
        pandas.Series: CCI values.
    """
    return talib.CCI(data['High'], data['Low'], data['Close'])

def calculate_mfi(data):
    """
    Calculate the Money Flow Index (MFI) for the given data.

    Args:
        data (pandas.DataFrame): DataFrame containing 'High', 'Low', 'Close', and 'Volume' data.

    Returns:
        pandas.Series: MFI values.
    """
    return talib.MFI(data['High'], data['Low'], data['Close'], data['Volume'])
