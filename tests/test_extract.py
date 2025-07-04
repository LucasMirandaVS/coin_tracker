from scripts.extract import extract_historical_data
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_extract_historical_data_returns_dataframe():
    df = extract_historical_data('bitcoin', days='1')
    assert df is not None
    assert not df.empty
    assert 'coin' in df.columns
    assert 'price_usd' in df.columns
