import configparser

# Initialize the configparser
config = configparser.ConfigParser()
config.read('config.ini')

# DataLoader settings
data_dir = config['DataLoader']['data_dir']
start_date = config['DataLoader']['start_date']
end_date = config['DataLoader']['end_date']

# Indicators settings
rsi_oversold = int(config['Indicators']['rsi_oversold'])
rsi_overbought = int(config['Indicators']['rsi_overbought'])
macd_threshold = int(config['Indicators']['macd_threshold'])
# ... and so on for other indicator settings

# ChartGenerator settings
min_volume = int(config['ChartGenerator']['min_volume'])
min_indicators = int(config['ChartGenerator']['min_indicators'])
rsi_check = config['ChartGenerator'].getboolean('rsi_check')
macd_check = config['ChartGenerator'].getboolean('macd_check')
# ... and so on for other ChartGenerator settings

# PatternDetection settings
pattern_data_dir = config['PatternDetection']['pattern_data_dir']
patterns_file = config['PatternDetection']['patterns_file']
