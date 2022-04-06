from django.contrib import admin
from .models import Document, Member

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
 

@admin.register(Member)
class SPNA_MemberAdmin(admin.ModelAdmin):
    """
    Member admin for the superuser(admin)
    """

    search_fields = ['nursery', 'town_or_city', 'county', 'country']
    list_display = (
        'nursery',
        'town_or_city',
        'country',
    )
    ordering = ('nursery',)
 