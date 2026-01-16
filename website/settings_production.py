from .settings import *

# Production overrides
DEBUG = False
ALLOWED_HOSTS = ["brueggerei.superservice-international.com"]

# WhiteNoise for static files
# MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": "media",
            "signature_version": "s3v4",
            "default_acl": None,
            "region_name": "auto",
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": "static",
            "signature_version": "s3v4",
            "default_acl": None,
            "region_name": "auto",
            "querystring_auth": False,  # No signed URLs for static files
        },
    },
}

# S3 settings
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL", "")


CSRF_TRUSTED_ORIGINS = [
    "https://brueggerei.superservice-international.com",
]