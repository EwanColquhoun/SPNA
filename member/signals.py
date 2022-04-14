from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SPNAMember

# Signals for the user.save() listener.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SPNAMember.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.spnamember.save()


# Helper functions used to save the SPNAMember instance

def save_spnamember(user, form):
    fname = get_fname(form)
    sname = get_sname(form)
    user.first_name = fname
    user.last_name = sname
    user.spnamember.fullname = form.cleaned_data['fullname']
    user.spnamember.nursery = form.cleaned_data['nursery']
    user.spnamember.street_address1 = form.cleaned_data['street_address1']
    user.spnamember.town_or_city = form.cleaned_data['town_or_city']
    user.spnamember.postcode = form.cleaned_data['postcode']
    user.spnamember.country = form.cleaned_data['country']
    user.spnamember.phone = form.cleaned_data['phone']
    user.spnamember.subscription = form.cleaned_data['subscription']
    user.spnamember.paid_until = '2022-02-23'
    user.spnamember.save()

def get_fname(fullname):
    fname = fullname.split()[0]
    return fname

def get_sname(fullname):
    sname = fullname.split()[1]
    return sname


