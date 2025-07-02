from extract import extract_all_coins
from validate import validate_crypto_data
from save_partitioned import save_partitioned_csv

if __name__ == "__main__":
    df = extract_all_coins(vs_currency='usd', days='90')
    df = validate_crypto_data(df)
    save_partitioned_csv(df)
