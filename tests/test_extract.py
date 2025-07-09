import pytest
from scripts.extract import extract_all_coins


def test_extract_all_coins_returns_dataframe():
    df = extract_all_coins(vs_currency="usd", days="1")
    assert not df.empty, "O DataFrame retornado está vazio."
    assert set(["coin", "date", "price_usd", "market_cap_usd", "volume_24h_usd"]).issubset(df.columns)
