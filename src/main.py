from services.ivoa_tap import fetch_raw_data
from services.s3_bucket import download_s3_file, load_csv_to_s3
import boto3
import pandas as pd
import io

# Main loop
if __name__ == "__main__":
    tap_service_url = "https://exoplanetarchive.ipac.caltech.edu/TAP"
    client = boto3.client('s3')

    try:
        # Fetch raw data from the IVOA TAP service
        raw_data = fetch_raw_data(tap_service_url)

        # Load the raw data to the S3 bucket
        load_csv_to_s3(client, raw_data, "s-nasa-exoplanet", "raw_data.csv")

        # Download the file from S3
        downloaded_data = download_s3_file(client, "s-nasa-exoplanet", "raw_data.csv")

        # Convert the downloaded bytes to a pandas DataFrame
        df = pd.read_csv(io .BytesIO(downloaded_data["Body"].read()))
        print("Downloaded DataFrame:")
        print(df.head())  # Display the first few rows of the DataFrame

    except Exception as e:
        print(f"Error occurred: {e}")