from django.db import models

# Create your models here.

class Document(models.Model):
    """
    A model for generating news and campaign articles
    """

    class Meta:
        """To correct the Django admin page"""
        verbose_name_plural = "Documents"

    title = models.CharField(max_length=255, null=True, blank=True)
    doc = models.FileField(upload_to='uploads/')
    date_uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)

