# List exchanges
First we can list exchanges to choose the best suitable option

```bash
freqtrade list-exchanges
```

# Generate basic configuration file
We need to generate a basic configuraiton file to be able to execute other commands and keep exploring the options.

```bash
freqtrade new-config --config user_data/config.json
```

# Pairlist filtering
To select pairlists by volume, we can add a filter to the configuration file. For example, to limit by volume and select the top 10 traded coins, add the following in the config json:

```json
"pairlists": [{ "method": "VolumePairList",
                "number_assets": 10,
                "sort_key": "quoteVolume",
                "min_value": 0,
                "refresh_period": 86400,
                "lookback_days": 90
             }]
```

This can be done to select pairlists automatically but we call this once to determine a static pairlist.

To generate this pairlist with quote currency USDC, run the following command:

```bash
freqtrade list-pairs -c config_binance.json --all --quote USDC --print-list
```

# Download data
