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
To select pairlists by volume, we can add a filter to the configuration file. For example, to limit by volume and select the top 20 traded coins, add the following in the config json:

```json
"pairlists": [{ "method": "VolumePairList",
                "number_assets": 20,
                "sort_key": "quoteVolume",
                "min_value": 0,
                "refresh_period": 86400,
                "lookback_days": 90
             }]
```

This can be done to select pairlists automatically but we call this once to determine a static pairlist.

To generate this pairlist with quote currency USDC, run the following command:

```bash
freqtrade test-pairlist -c ./user_data/config.json
```

This will give us a list of the top 20 pairs filtered by volume. For example:

```json
["BTC/USDC", "ETH/USDC", "XRP/USDC", "SOL/USDC", "FDUSD/USDC", "DOGE/USDC", "ADA/USDC", "SUI/USDC", "PEPE/USDC", "EUR/USDC", "HBAR/USDC", "LINK/USDC", "LTC/USDC", "AVAX/USDC", "DOT/USDC", "SHIB/USDC", "ENA/USDC", "WIF/USDC", "RUNE/USDC", "AAVE/USDC"]
```

# Download data
Now, we need to download the data for these pairlists. To do that, change the pairlist filtering method to Static:

```json
    "pairlists": [
        { "method": "StaticPairList" }
    ]
```

And add the pairlists to the `exchange.pair_whitelist` attribute in `config.json`:

```json
"exchange": {
        "name": "binance",
        "key": "",
        "secret": "",
        "ccxt_config": {},
        "ccxt_async_config": {},
        "pair_whitelist": ["BTC/USDC", "ETH/USDC", "XRP/USDC", "SOL/USDC", "FDUSD/USDC", "DOGE/USDC", "ADA/USDC", "SUI/USDC", "PEPE/USDC", "EUR/USDC", "HBAR/USDC", "LINK/USDC", "LTC/USDC", "AVAX/USDC", "DOT/USDC", "SHIB/USDC", "ENA/USDC", "WIF/USDC", "RUNE/USDC", "AAVE/USDC"],
        "pair_blacklist": [
            "BNB/.*"
        ]
```

Then, we are good to go to start downloading data for backtesting. To download data for the selected pairlists, for the timeframes `["5m", "15m", "1h", "4h", "1d"]` in the last 3 years, run the following command:

```bash
freqtrade download-data --exchange binance --pairs BTC/USDC ETH/USDC XRP/USDC SOL/USDC FDUSD/USDC DOGE/USDC ADA/USDC SUI/USDC PEPE/USDC EUR/USDC HBAR/USDC LINK/USDC LTC/USDC AVAX/USDC DOT/USDC SHIB/USDC ENA/USDC WIF/USDC RUNE/USDC AAVE/USDC --timeframes 5m 15m 1h 4h 1d --days 1095
```