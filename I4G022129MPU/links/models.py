from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

Author = get_user_model()

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    accessible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.target_url