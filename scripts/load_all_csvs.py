import os
import pandas as pd
from dotenv import load_dotenv

# Pegando as credenciais
load_dotenv()

# Define credencial explicitamente com caminho absoluto
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

def load_all_csvs(data_dir='data/') -> pd.DataFrame:
    """
    Lê todos os arquivos CSV dentro de subpastas de data/ e retorna um DataFrame unificado.
    """
    all_data = []

    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                print(f"📥 Lendo {file_path}")
                df = pd.read_csv(file_path, parse_dates=['date'])
                all_data.append(df)

    if not all_data:
        raise ValueError("Nenhum arquivo CSV encontrado!")

    full_df = pd.concat(all_data, ignore_index=True)
    print(f"✅ Total de registros unificados: {len(full_df)}")
    return full_df

# Execução isolada
if __name__ == "__main__":
    df = load_all_csvs()
    print(df.head())
