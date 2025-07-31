# tests/test_upload_to_gcs.py
import pytest
from unittest.mock import patch, MagicMock
from scripts.upload_to_gcs import upload_folder_to_gcs


def test_upload_to_gcs_walks_through_files(sample_crypto_df):
    with patch("scripts.upload_to_gcs.Path.rglob") as mock_rglob, \
         patch("scripts.upload_to_gcs.storage.Client") as mock_storage_client:

        mock_file = MagicMock()
        mock_file.relative_to.return_value = "2024-06/bitcoin.csv"
        mock_file.__str__.return_value = "data/2024-06/bitcoin.csv"
        mock_rglob.return_value = [mock_file]

        mock_bucket = MagicMock()
        mock_blob = MagicMock()
        mock_bucket.blob.return_value = mock_blob
        mock_storage_client.return_value.bucket.return_value = mock_bucket

        upload_folder_to_gcs("crypto_data", bucket_name="mock_bucket")

        mock_blob.upload_from_filename.assert_called_with("data/2024-06/bitcoin.csv")
