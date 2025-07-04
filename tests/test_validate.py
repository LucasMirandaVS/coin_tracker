from scripts.validate import validate_crypto_data
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_validate_crypto_data_passes(sample_crypto_df):
    validated = validate_crypto_data(sample_crypto_df)
    assert validated is not None
    assert not validated.empty
    assert 'date' in validated.columns
    assert validated['price_usd'].notnull().all()
