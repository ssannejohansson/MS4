import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Load env.py locally if it exists (optional)
if os.path.isfile("env.py"):
    import env

# Read AWS credentials and bucket from environment variables
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_REGION = "eu-north-1"

# Check if variables are set
print("AWS_ACCESS_KEY_ID:", AWS_ACCESS_KEY_ID)
print("AWS_SECRET_ACCESS_KEY:", AWS_SECRET_ACCESS_KEY)
print("AWS_STORAGE_BUCKET_NAME:", AWS_STORAGE_BUCKET_NAME)

if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY or not AWS_STORAGE_BUCKET_NAME:
    raise Exception("AWS credentials or bucket name are missing!")

# Create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Test: list objects in bucket
try:
    response = s3.list_objects_v2(Bucket=AWS_STORAGE_BUCKET_NAME)
    print("Bucket contents:", response.get("Contents", []))
except ClientError as e:
    print("Error accessing bucket:", e)

# Test: upload a small test file
test_filename = "s3_test_file.txt"
with open(test_filename, "w") as f:
    f.write("This is a test file for S3 upload.")

try:
    s3.upload_file(
        Filename=test_filename,
        Bucket=AWS_STORAGE_BUCKET_NAME,
        Key=f"test/{test_filename}"
    )
    print(f"Successfully uploaded {test_filename} to S3 in folder 'test/'")
except NoCredentialsError:
    print("No AWS credentials found.")
except ClientError as e:
    print("Failed to upload test file:", e)

# Optional: cleanup test file locally
os.remove(test_filename)
