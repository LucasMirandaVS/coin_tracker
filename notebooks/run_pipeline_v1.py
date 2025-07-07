# run_pipeline.py
from scripts.extract import extract_all_coins
from scripts.validate import validate_crypto_data
from scripts.save_partitioned import save_partitioned_csv
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    print("Iniciando extração...")
    df = extract_all_coins(vs_currency='usd', days='90') 
    print("Extração concluída.")

    print("🔍 Validando dados...")
    df = validate_crypto_data(df)
    print("Validação concluída.")

    print("Salvando CSVs particionados...")
    save_partitioned_csv(df, output_dir='data/')
    print("Pipeline finalizada com sucesso!")
