import pytest
import pandas as pd
from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def sample_crypto_df():
    return pd.DataFrame([
        {
            'date': pd.to_datetime('2024-06-01'),
            'coin': 'bitcoin',
            'price_usd': 65000.0,
            'market_cap_usd': 1200000000000.0,
            'volume_24h_usd': 35000000000.0
        },
        {
            'date': pd.to_datetime('2024-06-02'),
            'coin': 'ethereum',
            'price_usd': 3200.0,
            'market_cap_usd': 400000000000.0,
            'volume_24h_usd': 15000000000.0
        }
    ])
