
import pytest
from scripts.validate import validate_data, save_partitioned_csvs
import pandas as pd

def test_validate_data(sample_crypto_df):
    validated_df = validate_data(sample_crypto_df)

    # Deve remover linhas com valores nulos obrigatórios
    assert not validated_df.isnull().any().any()
    assert 'coin' in validated_df.columns
    assert validated_df["date"].dtype == "datetime64[ns]"


def test_save_partitioned_csvs(sample_crypto_df, tmp_path):
    output_dir = tmp_path / "data"
    save_partitioned_csvs(sample_crypto_df, output_dir=str(output_dir))

    # Verifica se ao menos um arquivo CSV foi criado
    csv_files = list(output_dir.rglob("*.csv"))
    assert len(csv_files) > 0

    # Verifica conteúdo do CSV
    for file in csv_files:
        df = pd.read_csv(file)
        assert "coin" in df.columns
        assert not df.empty
