from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """Storage for static files."""
    location = getattr(settings, "STATICFILES_LOCATION", "static")
    file_overwrite = True
    default_acl = None  # Let bucket policy control ACL


class MediaStorage(S3Boto3Storage):
    """Storage for user-uploaded media."""
    location = getattr(settings, "MEDIAFILES_LOCATION", "media")
    file_overwrite = False
    default_acl = None  # Let bucket policy control ACL


def get_default_settings(self):
    settings = super().get_default_settings()
    settings["default_acl"] = "public-read"
    return settings
