def list_s3_buckets(client):
    for bucket in client.list_buckets()['Buckets']:
        print(bucket['Name'])

def load_pandas_to_s3(client,df, bucket_name, file_name):
    """
    Load a pandas DataFrame to an S3 bucket as a CSV file.

    Parameters:
    df (pandas.DataFrame): The DataFrame to upload.
    bucket_name (str): The name of the S3 bucket.
    file_name (str): The name of the file to create in the S3 bucket.

    Returns:
    None
    """
    # Convert DataFrame to CSV
    csv_buffer = df.to_csv(index=False)

    # Upload CSV to S3
    client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer)  