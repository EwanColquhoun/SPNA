from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django import utils


class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        fname = self.get_fname(data)
        sname = self.get_sname(data)
        user.first_name = fname
        user.last_name = sname
        user._fullname = data['fullname']
        user.email = data["email"]
        user._street_address1 = data['street_address1']
        user._town_or_city = data['town_or_city']
        user._postcode = data['postcode']
        user._country = data['country']
        user._phone = data['phone']
        user._subscription = data['subscription']
     
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        user.save()
        print('adapter savea', user)
        return user

    @classmethod
    def get_fname(self, data):
        fn = data['fullname']
        fname = fn.split()[0]
        return fname

    @classmethod
    def get_sname(self, data):
        sn = data['fullname']
        sname = sn.split()[1]
        return sname


    #     class MyAccountAdapter(DefaultAccountAdapter):
    # def save_user(self, request, user, form, commit=True):
    #     data = form.cleaned_data
    #     user.first_name = data["first_name"]
    #     user.last_name = data["last_name"]
    #     user.email = data["email"]
    #     user.username = data["username"]
    #     user.phone = data['phone']
    #     user.birth_date = data['birth_date']
    #     user.city = data['city']
    #     user.address = data['address']
    #     if "password1" in data:
    #         user.set_password(data["password1"])
    #     else:
    #         user.set_unusable_password()
    #     self.populate_username(request, user)
    #     user.save()
    #     return user