import requests
import pandas as pd
from datetime import datetime
import time
import os
from dotenv import load_dotenv

load_dotenv()

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")


# Lista das moedas que você escolheu
COINS = ['bitcoin', 'ethereum', 'solana', 'binancecoin', 'ripple']

# Função para extrair dados históricos
def extract_historical_data(coin_id, vs_currency='usd', days='30', interval='daily'):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
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
            price_timestamp = prices[i][0]
            date = datetime.utcfromtimestamp(price_timestamp / 1000).strftime('%Y-%m-%d')
            row = {
                'date': date,
                'coin': coin_id,
                'price_usd': prices[i][1],
                'market_cap_usd': market_caps[i][1] if i < len(market_caps) else None,
                'volume_24h_usd': total_volumes[i][1] if i < len(total_volumes) else None
            }
            rows.append(row)
        
        df = pd.DataFrame(rows)
        return df

    except Exception as e:
        print(f"Erro ao extrair dados de {coin_id}: {e}")
        return pd.DataFrame()

# Função para extrair todas as moedas da lista
def extract_all_coins(vs_currency='usd', days='30'):
    all_dfs = []
    for coin in COINS:
        print(f"Extraindo dados para {coin}...")
        df = extract_historical_data(coin, vs_currency, days)
        if not df.empty:
            all_dfs.append(df)
        time.sleep(1)  # Respeitar limite da API

    if all_dfs:
        full_df = pd.concat(all_dfs, ignore_index=True)
        return full_df
    else:
        return pd.DataFrame()

# Execução de teste
if __name__ == "__main__":
    df = extract_all_coins(vs_currency='usd', days='90')
    print(df.head())
    df.to_csv('../data/crypto_data.csv', index=False)
