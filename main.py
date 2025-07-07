import os
from dotenv import load_dotenv
from google.cloud import bigquery
from scripts.load_all_csvs import load_all_csvs

# Carrega variáveis de ambiente
load_dotenv()

# Define variáveis do projeto
PROJECT_ID = "projeto-estudando-gcp"
DATASET_ID = "crypto_dataset"
TABLE_ID = "moedas_particionadas"

# Configura caminho da credencial (usando .env)
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

def run_pipeline():
    print("Lendo arquivos CSV particionados...")
    df = load_all_csvs("data")
    print(f"Total de registros unificados: {len(df)}")

    print("Subindo dados para o BigQuery...")
    client = bigquery.Client(project=PROJECT_ID)

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        time_partitioning=bigquery.TimePartitioning(field="date"),
    )

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()

    print(f"Dados carregados com sucesso: {len(df)} linhas inseridas.")

if __name__ == "__main__":
    run_pipeline()
