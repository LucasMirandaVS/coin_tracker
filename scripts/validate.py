# scripts/validate_partition.py
import pandas as pd
import os
from pathlib import Path


def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = {"coin", "date", "price_usd", "market_cap_usd", "volume_24h_usd"}
    if not required_columns.issubset(df.columns):
        raise ValueError("DataFrame faltando colunas obrigatórias")

    df = df.dropna(subset=["coin", "date", "price_usd"])
    df["date"] = pd.to_datetime(df["date"])
    return df


def save_partitioned_csvs(df: pd.DataFrame, output_dir: str = "data"):
    df = validate_data(df)
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for (coin, month), group in df.groupby(["coin", df["date"].dt.to_period("M")]):
        month_str = str(month)
        folder = Path(output_dir) / month_str
        folder.mkdir(parents=True, exist_ok=True)
        file_path = folder / f"{coin}.csv"
        group.to_csv(file_path, index=False)
        print(f"Salvo: {file_path}")
