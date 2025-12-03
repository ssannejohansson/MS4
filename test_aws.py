import boto3
import os
from botocore.exceptions import ClientError

# Ensure AWS credentials are set
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'the-poster-vault'
AWS_REGION = 'eu-north-1'

print("AWS_ACCESS_KEY_ID:", AWS_ACCESS_KEY_ID)
print("AWS_SECRET_ACCESS_KEY:", AWS_SECRET_ACCESS_KEY)

# Create S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Try listing objects in the bucket
try:
    response = s3.list_objects_v2(Bucket=AWS_STORAGE_BUCKET_NAME)
    print("Bucket contents:")
    if 'Contents' in response:
        for obj in response['Contents']:
            print(" -", obj['Key'])
    else:
        print("Bucket is empty")
except ClientError as e:
    print("ERROR:", e)
