# Crypto Data Pipeline

A lightweight and containerized pipeline for collecting historical cryptocurrency data and uploading it to Google BigQuery.

This project was built using **Google BigQuery** for scalable data storage and analytics, **Cloud Run** to deploy the containerized pipeline, and **Cloud Scheduler** to automate its execution on a weekly basis. The entire workflow is orchestrated using **Docker** for easy packaging and reproducibility.

The final report is visualized in a dynamic dashboard built with **Looker Studio**, available at:

🔗 [View Dashboard](https://lookerstudio.google.com/reporting/45d260d1-7c90-4712-832d-ce907618e626/page/FSZQF/edit)

## Project Structure

```
crypto_data_pipeline/
├── data/                     # CSV files organized by month and coin
│   └── 2025-07/
│       ├── bitcoin.csv
│       ├── ethereum.csv
│       └── ...
├── scripts/                 # Python modules
│   ├── __init__.py
│   ├── load_all_csvs.py
│   └── upload_to_bigquery.py
├── secrets/                 # GCP credentials (excluded from version control)
│   └── project-credentials.json
├── .gitignore
├── main.py                  # Pipeline entrypoint
├── requirements.txt
└── README.md                # Documentation
├── Dockerfile               # Docker and Docker Compose setup
└── docker-compose.yml
```

---

## What the pipeline does

1. Loads all CSVs from the `data/` folder (recursively)
2. Concatenates the data into a unified DataFrame
3. Uploads the data to a partitioned table in BigQuery
4. Data is displayed in a dashboard in Looker Studio

---

##  How to Run Locally

### Requirements:
- Python 3.12+
- Google Cloud credentials in JSON format
- CoinGecko API Key
- BigQuery dataset already created

### Environment Variables:
Create a `.env` file with:
```
GOOGLE_APPLICATION_CREDENTIALS=secrets/project-credentials.json
COINGECKO_API_KEY=insertyourapikeyhere
```

## Run with Docker

### Build and run
```bash
docker compose up --build
```

> Make sure the credentials file exists in `secrets/` and is mapped inside the container.

---

## GCP Costs (approximate)
- **BigQuery storage**: First 10 GB free, then $0.02/GB/month
- **BigQuery queries**: 1 TB free/month, then $5/TB
- **Cloud Run job**: Charged only while running (first 2 million requests free/month)
- **Cloud Scheduler**: Free up to 3 jobs/month

---

## Future Improvements
- Enable logging and alerting
- Validate schema before upload
- Connect to Looker Studio (ex-Google Data Studio)
- Parametrize coin list or add CLI options
