import talib

# Define indicator thresholds (you can adjust these values as needed)
rsi_oversold = 30
rsi_overbought = 70
macd_threshold = 0
stoch_oversold = 20
stoch_overbought = 80
cci_oversold = -100
cci_overbought = 100
mfi_oversold = 30
mfi_overbought = 70

# Define functions to calculate each indicator

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

def get_most_recent_signal(data):
    """
    Calculate the most recent values of various technical indicators.

    Args:
        data (pandas.DataFrame): DataFrame containing financial data.

    Returns:
        dict: A dictionary with indicator names as keys and their most recent values as values.
    """
    signals = {
        'RSI': calculate_rsi(data),
        'MACD': calculate_macd(data),
        'Stochastic_K': calculate_stochastic(data)[0],
        'Stochastic_D': calculate_stochastic(data)[1],
        'CCI': calculate_cci(data),
        'MFI': calculate_mfi(data),
    }
    return signals

def generate_rsi_signals(data):
    """
    Generate buy/sell signals based on the Relative Strength Index (RSI).

    Args:
        data (pandas.DataFrame): DataFrame containing indicator data.

    Returns:
        tuple: Two boolean values representing the RSI buy and sell signals.
    """
    rsi_data = data['RSI']
    rsi_buy_signal = (rsi_data < rsi_oversold)
    rsi_sell_signal = (rsi_data > rsi_overbought)
    return rsi_buy_signal, rsi_sell_signal

def generate_macd_signals(data):
    """
    Generate buy/sell signals based on the Moving Average Convergence Divergence (MACD).

    Args:
        data (pandas.DataFrame): DataFrame containing indicator data.

    Returns:
        tuple: Two boolean values representing the MACD buy and sell signals.
    """
    macd_data = data['MACD']
    macd_buy_signal = (macd_data > macd_threshold)
    macd_sell_signal = (macd_data < macd_threshold)
    return macd_buy_signal, macd_sell_signal

def generate_stoch_signals(data):
    """
    Generate buy/sell signals based on the Stochastic Oscillator (K and D).

    Args:
        data (pandas.DataFrame): DataFrame containing indicator data.

    Returns:
        tuple: Two boolean values representing the Stochastic buy and sell signals.
    """
    k_data = data['Stochastic_K']
    d_data = data['Stochastic_D']
    stoch_buy_signal = (k_data < stoch_oversold) & (d_data < stoch_oversold)
    stoch_sell_signal = (k_data > stoch_overbought) & (d_data > stoch_overbought)
    return stoch_buy_signal, stoch_sell_signal

def generate_cci_signals(data):
    """
    Generate buy/sell signals based on the Commodity Channel Index (CCI).

    Args:
        data (pandas.DataFrame): DataFrame containing indicator data.

    Returns:
        tuple: Two boolean values representing the CCI buy and sell signals.
    """
    cci_data = data['CCI']
    cci_buy_signal = (cci_data < cci_oversold)
    cci_sell_signal = (cci_data > cci_overbought)
    return cci_buy_signal, cci_sell_signal

def generate_mfi_signals(data):
    """
    Generate buy/sell signals based on the Money Flow Index (MFI).

    Args:
        data (pandas.DataFrame): DataFrame containing indicator data.

    Returns:
        tuple: Two boolean values representing the MFI buy and sell signals.
    """
    mfi_data = data['MFI']
    mfi_buy_signal = (mfi_data < mfi_oversold)
    mfi_sell_signal = (mfi_data > mfi_overbought)
    return mfi_buy_signal, mfi_sell_signal
