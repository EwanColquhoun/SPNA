from django.contrib.auth.models import AbstractUser, UserManager, User
from django_countries.fields import CountryField
from django.db import models

# Create your models here.

CATEGORIES = (
    ('1', 'Media Releases'),
    ('2', 'Media Mentions'),
    ('3', 'Letters to and responses from Government'))

class Document(models.Model):
    """
    A model for generating news and campaign articles
    """

    class Meta:
        """To correct the Django admin page"""
        verbose_name_plural = "Documents"

    title = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        default=False)
    doc = models.FileField(upload_to='uploads/')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


    def __str__(self):
        return str(self.title)

    
class Member(models.Model):
    """
    Extends the default User into the Member class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nursery = models.CharField(max_length=255, unique=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=False, blank=False)
    objects = UserManager()

    def __str__(self):
        return str(self.user)