import os
import pandas as pd


def save_partitioned_csv(df: pd.DataFrame, output_dir: str = 'data/'):
    """
    Salva o DataFrame em arquivos CSV particionados por mês e moeda.

    Exemplo:
    data/2024-06/bitcoin.csv
    data/2024-06/ethereum.csv
    """
    if df.empty:
        raise ValueError("DataFrame está vazio. Nada a salvar.")

    df['year_month'] = df['date'].dt.to_period('M').astype(str)

    for (year_month, coin), group in df.groupby(['year_month', 'coin']):
        folder_path = os.path.join(output_dir, year_month)
        os.makedirs(folder_path, exist_ok=True)

        filepath = os.path.join(folder_path, f"{coin}.csv")
        group.drop(columns='year_month').to_csv(filepath, index=False)
        print(f"✅ CSV salvo: {filepath}")
