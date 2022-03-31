from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Articles


@admin.register(Articles)
class ArticleAdmin(SummernoteModelAdmin):
    """
    Article admin for the superuser(admin)
    """
    # prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content', 'created_on', 'campaign']
    list_display = (
        'title',
        'content',
        'created_on',
        'image_url',
        'image',
        'campaign',
    )
    ordering = ('created_on',)
    summernote_fields = ('content')
