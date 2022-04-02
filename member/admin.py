from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Documents admin for the superuser(admin)
    """

    search_fields = ['title', 'date_uploaded']
    list_display = (
        'title',
        'date_uploaded',
    )
    ordering = ('-date_uploaded',)
 
