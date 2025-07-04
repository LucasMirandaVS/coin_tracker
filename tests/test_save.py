import os
import shutil
from scripts.save_partitioned import save_partitioned_csv
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_save_partitioned_csv_creates_files(sample_crypto_df):
    test_dir = 'data/test_output'
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

    save_partitioned_csv(sample_crypto_df, output_dir=test_dir)

    files_created = []
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            files_created.append(file)

    assert 'bitcoin.csv' in files_created or 'ethereum.csv' in files_created

    # Limpeza
    shutil.rmtree(test_dir)
