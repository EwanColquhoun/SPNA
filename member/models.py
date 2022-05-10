import datetime
from datetime import date
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.conf import settings
from django.db import models

# Create your models here.

class Plan(models.Model):
    """ Creates the subscription plans in the backend for security."""
    name = models.CharField(max_length=256)
    amount = models.IntegerField()
    disp_amount = models.IntegerField(default='0')
    objects = UserManager()


class Document(models.Model):
    """
    A model for generating news and campaign articles
    """
    CATEGORIES = (
    ('1', 'Media Releases'),
    ('2', 'Media Mentions'),
    ('3', 'Letters to and responses from Government'))

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

    
class SPNAMember(models.Model):
    """
    Extends the default User into the Member class
    """
    M = 'Monthly'
    M6 = 'Six Monthly'
    Y = 'Yearly'

    PLAN = (
        (M, '£10 monthly'),
        (M6, '£55 six monthly'),
        (Y, '£100 yearly'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nursery = models.CharField(max_length=255)
    fullname = models.CharField(max_length=50, null=False, blank=False, default='')
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    subscription = models.CharField(max_length=16, choices=PLAN, default=1, null=False, blank=False)
    paid_until = models.DateField(null=True, blank=True)
    paid = models.BooleanField(null=True, blank=True, default=False)
    stripe_id = models.CharField(max_length=255)
    sub_id = models.CharField(max_length=255)
    has_cancelled = models.BooleanField(default=False)
    objects = UserManager()

    def __str__(self):
        return str(self.fullname)

# Below methods from https://www.youtube.com/watch?v=Mw__Pw1iGgA

    def set_paid_until(self, date_or_timestamp):
        """
        Sets the paid until date based on stripe wh return
        """
        if isinstance(date_or_timestamp, int):
            # input date as timestamp integer
            paid_until = date.fromtimestamp(date_or_timestamp)
        elif isinstance(date_or_timestamp, str):
            # input date as timestamp string
            paid_until = date.fromtimestamp(int(date_or_timestamp))
        else:
            paid_until = date_or_timestamp

        self.paid_until = paid_until
        print('paid until', self.paid_until)
        self.save()

    def has_paid(
        self,
        current_date=datetime.date.today()
    ):
        """
        Defines if spnamember has paid according to stripe wh return
        """
        if self.paid_until is None:
            self.paid = False
        elif current_date < self.paid_until:
            self.paid = True

        self.save()
