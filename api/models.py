from django.db import models


# Create your models here.
class Video(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=500, blank=False, db_index=True)
    published_at = models.DateTimeField(blank=False, db_index=True)
    description = models.TextField(max_length=5000, blank=True)
    thumbnail_url = models.URLField(blank=False)
    search_query = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.title
