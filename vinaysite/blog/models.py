from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length='45')
    text=models.TextField()
    published_date=models.DateTimeField(blank=True,null=True)
    create_date=models.DateTimeField(default=timezone.now())

    def publish(self):
        return self.published_date= timezone.now()
        self.save()
