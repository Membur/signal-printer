import os
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from indicators import calculate_rsi, calculate_macd, calculate_stochastic, calculate_cci, calculate_mfi

# Define indicator thresholds (you can adjust these as needed)
rsi_oversold = 30
rsi_overbought = 70
macd_threshold = 0
stoch_oversold = 20
stoch_overbought = 80
cci_oversold = -100
cci_overbought = 100
mfi_oversold = 30
mfi_overbought = 70
min_volume = 10000000

def get_most_recent_signal(data):
    signals = []

    # Calculate RSI
    rsi = calculate_rsi(data)
    rsi_buy_signal = (rsi.iloc[-1] < rsi_oversold)
    rsi_sell_signal = (rsi.iloc[-1] > rsi_overbought)
    signals.append(('RSI Buy', rsi_buy_signal))
    signals.append(('RSI Sell', rsi_sell_signal))

    # Calculate MACD
    macd = calculate_macd(data)
    macd_buy_signal = (macd.iloc[-1] > macd_threshold)
    macd_sell_signal = (macd.iloc[-1] < macd_threshold)
    signals.append(('MACD Buy', macd_buy_signal))
    signals.append(('MACD Sell', macd_sell_signal))

    # Calculate Stochastic Oscillator
    k, d = calculate_stochastic(data)
    stoch_buy_signal = (k.iloc[-1] < stoch_oversold)
    stoch_sell_signal = (k.iloc[-1] > stoch_overbought)
    signals.append(('Stochastic Buy', stoch_buy_signal))
    signals.append(('Stochastic Sell', stoch_sell_signal))

    # Calculate Commodity Channel Index (CCI)
    cci = calculate_cci(data)
    cci_buy_signal = (cci.iloc[-1] < cci_oversold)
    cci_sell_signal = (cci.iloc[-1] > cci_overbought)
    signals.append(('CCI Buy', cci_buy_signal))
    signals.append(('CCI Sell', cci_sell_signal))

    # Calculate Money Flow Index (MFI)
    mfi = calculate_mfi(data)
    mfi_buy_signal = (mfi.iloc[-1] < mfi_oversold)
    mfi_sell_signal = (mfi.iloc[-1] > mfi_overbought)
    signals.append(('MFI Buy', mfi_buy_signal))
    signals.append(('MFI Sell', mfi_sell_signal))

    return signals

def generate_chart(symbol, start_date, end_date, data_dir, min_indicators=1):
    data = yf.download(symbol, start=start_date, end=end_date, interval="1wk")

    # Check the minimum volume threshold
    if data['Volume'].iloc[-1] < min_volume:
        print(f"Volume for {symbol} is below the minimum threshold. Skipping...")
        return

    signals = get_most_recent_signal(data)

    # Check if at least min_indicators indicators generated signals
    active_signals = [indicator for indicator, signal in signals if signal]
    if len(active_signals) < min_indicators:
        print(f"Not enough active signals ({len(active_signals)}) for {symbol}. Skipping...")
        return

    data.to_csv(os.path.join(data_dir, '1wk-data', f'{symbol}_data.csv'))

    fig = go.Figure()

    candlestick = go.Candlestick(
        x=data.index.astype(str),
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Candlestick',
        increasing_line_color='green',
        decreasing_line_color='red'
    )

    fig.add_trace(candlestick)

    vertical_offset = 0  # Initialize vertical offset

    for indicator, signal in signals:
        if 'Buy' in indicator and signal:
            signal_arrow = go.Scatter(
                x=[data.index[-1]],
                y=[data['Low'].iloc[-1] + vertical_offset],  # Apply vertical offset
                mode='markers+text',
                marker=dict(symbol='triangle-up', size=12, color='green'),
                text=['BUY'],
                textposition="bottom center",
                name=f'{indicator} Signal'
            )

            fig.add_trace(signal_arrow)

            vertical_offset += 0.5  # Adjust the vertical offset for the next indicator

        if 'Sell' in indicator and signal:
            signal_arrow = go.Scatter(
                x=[data.index[-1]],
                y=[data['Low'].iloc[-1] - vertical_offset],  # Apply vertical offset
                mode='markers+text',
                marker=dict(symbol='triangle-down', size=12, color='red'),
                text=['SELL'],
                textposition="bottom center",
                name=f'{indicator} Signal'
            )

            fig.add_trace(signal_arrow)

            vertical_offset += 0.5  # Adjust the vertical offset for the next indicator

    title_text = f'<a href="https://www.tradingview.com/symbols/{symbol}/" target="_blank">{symbol}</a> 1 Week Signals'

    fig.update_layout(
        title=title_text,
        xaxis_title="Date",
        yaxis_title="Price",
        showlegend=True,
        template='plotly_dark'
    )

    chart_file = os.path.join(data_dir, '1wk-charts', f'{symbol}_signals_1wk.html')
    fig.write_html(chart_file)
    print(f"Chart saved as {chart_file}")

def main():
    data_dir = 'C:/Users/Sean/Documents/Python Scripts/signal-printer/'
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(os.path.join(data_dir, '1wk-charts'), exist_ok=True)
    os.makedirs(os.path.join(data_dir, '1wk-data'), exist_ok=True)

    with open('tools/symbols.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]

            try:
                generate_chart(
                    symbol,
                    start_date="2022-10-01",
                    end_date="2023-08-09",
                    data_dir=data_dir,
                    min_indicators=1,  # Set the minimum number of required indicators
                )
            except Exception as e:
                print(f"Failed to generate chart for symbol {symbol}: {e}")

if __name__ == "__main__":
    main()