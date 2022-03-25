from django.contrib import admin
from .models import Articles


class ArticleAdmin(admin.ModelAdmin):
    """
    Article admin for the superuser(admin)
    """
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content', 'created_on', 'campaign']
    list_display = (
        'title',
        'slug',
        'content',
        'created_on',
        'image_url',
        'image',
        'campaign',
    )
    ordering = ('created_on',)

admin.site.register(Articles, ArticleAdmin)
