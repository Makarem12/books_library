from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

class book(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    title = models.CharField(max_length=60, blank=False, null=False)
    description = models.TextField(max_length=200)
    rating = models.CharField(max_length=60)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title