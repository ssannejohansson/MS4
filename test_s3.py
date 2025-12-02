# test_s3.py
import os

# Make sure env.py runs first
if os.path.isfile('env.py'):
    import env

import boto3

# Now these variables are guaranteed to exist
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name="eu-north-1"
)

bucket_name = os.environ.get("AWS_STORAGE_BUCKET_NAME")
print("Bucket name:", bucket_name)  # debug line to make sure it's set

response = s3.list_objects_v2(Bucket=bucket_name)
print(response)
