from django.db import models


class Articles(models.Model):
    """
    A model for generating news and campaign articles
    """
    class Meta:
        verbose_name = 'Articles'

    title = models.CharField(max_length=256, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    campaign = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.title)