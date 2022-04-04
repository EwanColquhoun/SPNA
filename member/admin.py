from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Documents admin for the superuser(admin)
    """

    search_fields = ['title', 'category', 'date_uploaded']
    list_display = (
        'title',
        'category',
        'date_uploaded',
    )
    ordering = ('-date_uploaded',)
 
