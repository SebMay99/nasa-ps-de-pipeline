from services.ivoa_tap import fetch_raw_data
from services.s3_bucket import load_pandas_to_s3
import boto3

# Main loop
if __name__ == "__main__":
    tap_service_url = "https://exoplanetarchive.ipac.caltech.edu/TAP"
    client = boto3.client('s3')

    try:
        # Fetch raw data from the IVOA TAP service
        raw_data = fetch_raw_data(tap_service_url)

        # Load the raw data to the S3 bucket
        load_pandas_to_s3(client, raw_data, "s-nasa-exoplanet", "raw_data.csv")

    except Exception as e:
        print(f"Error occurred: {e}")