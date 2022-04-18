from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """Sets location of static"""
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """Sets location of media"""
    location = settings.MEDIAFILES_LOCATION