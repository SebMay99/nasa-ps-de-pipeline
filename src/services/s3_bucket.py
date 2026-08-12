def list_s3_buckets(client):
    for bucket in client.list_buckets()['Buckets']:
        print(bucket['Name'])

def load_csv_to_s3(client,df, bucket_name, file_name):
    """
    Load a CSV file to an S3 bucket.

    Parameters:
    df: The DataFrame to upload.
    bucket_name (str): The name of the S3 bucket.
    file_name (str): The name of the file to create in the S3 bucket.

    Returns:
    None
    """
    try:
        print(f"Uploading DataFrame to S3 bucket '{bucket_name}' as '{file_name}'...")
        # Convert DataFrame to CSV
        csv_buffer = df.to_csv(index=False)

        # Upload CSV to S3
        client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer)  

        print(f"DataFrame uploaded to S3 bucket '{bucket_name}' as '{file_name}' successfully.")
    except Exception as e:
        print(f"Error occurred while uploading to S3: {e}")

def download_s3_file(client, bucket_name, file_name):
    """
    Download a file from an S3 bucket.

    Parameters:
    client: The S3 client.
    bucket_name (str): The name of the S3 bucket.
    file_name (str): The name of the file in the S3 bucket.

    Returns:
    bytes: The content of the downloaded file.
    """
    try:
        print(f"Downloading file '{file_name}' from S3 bucket '{bucket_name}'...")
        # Download the file from S3
        response = client.get_object(Bucket=bucket_name, Key=file_name)
        print(f"File '{file_name}' downloaded from S3 bucket '{bucket_name}' successfully.")
        return response  # Return the content of the file
    except Exception as e:
        print(f"Error occurred while downloading from S3: {e}")