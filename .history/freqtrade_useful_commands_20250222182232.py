# List exchanges
"freqtrade list-exchanges"

# Generate basic configuration file
"freqtrade new-config --config user_data/config.json"

# Once created the pairlist we can filter the pairs by volume adding the following config in pairlists
"pairlists": [{ "method": "VolumePairList",
                "number_assets": 20,
                "sort_key": "quoteVolume",
                "min_value": 0,
                "refresh_period": 86400,
                "lookback_days": 90
                }]

freqtrade list-pairs -c config_binance.json --all --base BTC ETH --quote USDT USD --print-listl

# Download data
