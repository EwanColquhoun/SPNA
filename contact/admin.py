from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact 


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Contact admin for the superuser(admin)
    """

    search_fields = ['name', 'email', 'created']
    list_display = (
        'name',
        'phone_number',
        'email',
        'replied',
        'created'
    )
    ordering = ('created',)
    summernote_fields = ('message')

    
