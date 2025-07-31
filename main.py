from scripts.extract import extract_all_coins
from scripts.validate import save_partitioned_csvs
from scripts.upload_to_gcs import upload_folder_to_gcs

# Atualizações para o novo projeto no GCP
BUCKET_NAME = "crypto-data-tracker"
GCS_FOLDER = "crypto_data"
LOCAL_OUTPUT_DIR = "data"

def run_pipeline():
    # 1. Extrair dados da API da CoinGecko (últimos 60 dias)
    print("Extraindo dados da API CoinGecko...")
    df = extract_all_coins(vs_currency='usd', days='60')

    if df.empty:
        print(" Nenhum dado extraído. Encerrando pipeline.")
        return

    # 2. Validar e particionar os dados localmente
    print(" Salvando arquivos particionados localmente...")
    save_partitioned_csvs(df, output_dir=LOCAL_OUTPUT_DIR)

    # 3. Enviar os arquivos particionados para o bucket no GCS
    print("Fazendo upload para o Google Cloud Storage...")
    upload_folder_to_gcs(
        bucket_name=BUCKET_NAME,
        local_folder=LOCAL_OUTPUT_DIR,
        gcs_folder=GCS_FOLDER
    )

    print("Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()
