# scripts/upload_to_gcs.py
from google.cloud import storage
from pathlib import Path

def upload_folder_to_gcs(local_folder: str, bucket_name: str, gcs_folder: str = ""):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    folder_path = Path(local_folder)

    for file_path in folder_path.rglob("*.csv"):
        relative_path = file_path.relative_to(folder_path)
        blob_path = f"{gcs_folder}/{relative_path}".strip("/")
        blob = bucket.blob(blob_path)
        blob.upload_from_filename(str(file_path))
        print(f"Upload concluído: {file_path} → gs://{bucket_name}/{blob_path}")
