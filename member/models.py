from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.conf import settings
from django.db import models

# Create your models here.

CATEGORIES = (
    ('1', 'Media Releases'),
    ('2', 'Media Mentions'),
    ('3', 'Letters to and responses from Government'))

PLAN = (
    (1, 'Monthly'),
    (2, '6 Monthly'),
    (3, 'Yearly'),
)

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

    
class SPNAMember(models.Model):
    """
    Extends the default User into the Member class
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nursery = models.CharField(max_length=255)
    fullname = models.CharField(max_length=50, null=False, blank=False, default='')
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=False, blank=False)
    subscription = models.CharField(max_length=10, choices=PLAN, default=1, null=False, blank=False)
    paid_until = models.DateField()
    objects = UserManager()

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create of update the member profile
    """
    
    if created:
        spnamember, created = SPNAMember.objects.get_or_create(user=instance)
