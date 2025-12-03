import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MS4.settings')
django.setup()

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def test_s3_upload():
    print("Default storage:", default_storage.__class__)

    # Name of the test file
    test_filename = 'heroku_test_file.txt'
    test_content = b'Hello from Heroku!'

    # Save file to default storage
    file_path = default_storage.save(test_filename, ContentFile(test_content))
    print("Saved file path:", file_path)

    # Get the file URL
    file_url = default_storage.url(test_filename)
    print("File URL:", file_url)

if __name__ == "__main__":
    test_s3_upload()
