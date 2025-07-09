import requests
import pandas as pd
from datetime import datetime, timezone
import time
import os
from dotenv import load_dotenv

load_dotenv()

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY") 
COINS = ['bitcoin', 'ethereum', 'solana', 'binancecoin', 'ripple']
BASE_URL = "https://api.coingecko.com/api/v3"

def extract_historical_data(coin_id, vs_currency='usd', days='60', interval='daily'):
    url = f"{BASE_URL}/coins/{coin_id}/market_chart"
    params = {
        'vs_currency': vs_currency,
        'days': days,
        'interval': interval
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        prices = data.get('prices', [])
        market_caps = data.get('market_caps', [])
        total_volumes = data.get('total_volumes', [])

        rows = []
        for i in range(len(prices)):
            date = datetime.utcfromtimestamp(prices[i][0] / 1000).strftime('%Y-%m-%d')
            rows.append({
                'coin': coin_id,
                'date': date,
                'price_usd': prices[i][1],
                'market_cap_usd': market_caps[i][1] if i < len(market_caps) else None,
                'volume_24h_usd': total_volumes[i][1] if i < len(total_volumes) else None
            })

        return pd.DataFrame(rows)

    except Exception as e:
        print(f"Erro ao extrair dados de {coin_id}: {e}")
        return pd.DataFrame()

def extract_all_coins(vs_currency='usd', days='60'):
    all_dfs = []
    for coin in COINS:
        print(f"Extraindo dados para {coin}...")
        df = extract_historical_data(coin, vs_currency, days)
        if not df.empty:
            all_dfs.append(df)
        time.sleep(1)  # Evita throttling

    if all_dfs:
        return pd.concat(all_dfs, ignore_index=True)
    else:
        return pd.DataFrame()

if __name__ == "__main__":
    df = extract_all_coins(days='90')
    print(df.head())
