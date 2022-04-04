from django.db import models
from django.core.validators import RegexValidator


REPLIED = ((1, 'No'), (2, 'Yes'))


class Contact(models.Model):
    """
    Initiates the contact model
    """
    name = models.CharField(max_length=30, null=False, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    email = models.EmailField(
        max_length=40,
        blank=False,
        help_text='Email must include "@"')
    message = models.TextField(blank=False, null=False)
    replied = models.IntegerField(choices=REPLIED, default=False)
    created = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.name)