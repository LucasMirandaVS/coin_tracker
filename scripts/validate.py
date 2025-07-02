import pandas as pd


def validate_crypto_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Valida os dados extraídos da API da CoinGecko.

    - Checa se dataframe está vazio
    - Verifica presença de colunas obrigatórias
    - Converte tipos e checa valores inválidos
    """
    if df.empty:
        raise ValueError("O dataframe está vazio.")

    expected_columns = ['date', 'coin', 'price_usd', 'market_cap_usd', 'volume_24h_usd']
    for col in expected_columns:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente: {col}")

    # Conversão de tipos
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['coin'] = df['coin'].astype(str)

    for col in ['price_usd', 'market_cap_usd', 'volume_24h_usd']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remover registros com data ou preço inválidos
    df = df.dropna(subset=['date', 'price_usd'])

    return df
