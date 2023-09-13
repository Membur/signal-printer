Stock Screener

The Stock Screener is a Python-based project that helps you analyze and visualize stock market data. This README will guide you through the steps to set up and use the Stock Screener effectively.
Table of Contents

    Getting Started
    Project Structure
    Configuration
    Fetching Data
    Generating Charts
    Pattern Detection
    Running the Stock Screener

Getting Started

To get started with the Stock Screener, follow these steps:

    Clone the project repository to your local machine.

    bash

git clone https://github.com/your-username/stock-screener.git

Install the required dependencies by running:

bash

    pip install -r requirements.txt

Project Structure

Before we dive into using the Stock Screener, let's understand the project's structure:

    charts/: This directory will contain the generated charts.
    fetched-data/: Here, you will find the stock market data fetched from Yahoo Finance in CSV format.
    datasets/symbols.csv: This CSV file should contain a list of stock symbols and their corresponding company names.

Configuration

You can configure the Stock Screener by editing the config.ini file. Here's how and where to change settings:

    Open the config.ini file in a text editor.

    In the [DataLoader] section, you can set the data_dir, start_date, and end_date for data loading.

    In the [Indicators] section, you can configure indicator thresholds. For example, you can change rsi_oversold, rsi_overbought, and other indicator values.

    In the [ChartGenerator] section, define settings for generating charts, such as min_volume and which indicators to check. To enable or disable an indicator check, set its corresponding option (e.g., rsi_check, macd_check) to true or false.

    In the [PatternDetection] section, configure settings for pattern detection. You can specify the pattern_data_dir and patterns_file.

    You can ignore the [Flask] section as it's not used in the project.

Fetching Data

Before analyzing stocks, you need to fetch data from Yahoo Finance. Run the following command to download data for the symbols in datasets/symbols.csv:

bash

python data_fetcher.py

This will create CSV files in the fetched-data/ directory.
Generating Charts

To generate charts and analyze stock data, use the chart_generator.py file. This script generates charts based on indicator signals. You can customize which indicators to use and the minimum requirements for generating a chart.

bash

python chart_generator.py

Generated charts will be saved in the charts/ directory.
Pattern Detection

The Stock Screener can detect candlestick patterns in stock data. The patterns to detect are defined in the patterns.py file. To detect patterns, use the following command:

bash

python pattern_detector.py

Detected patterns will be printed to the console.
Running the Stock Screener

Finally, to run the Stock Screener, use the main.py script. This script brings everything together, fetching data, generating charts, and detecting patterns:

bash

python main.py

Follow the on-screen prompts and the configurations in config.ini to analyze and screen stocks effectively.

Now you're ready to use the Stock Screener project to analyze and visualize stock market data. Happy screening!