from django.db import models
# from django.utils
from datetime import date


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(
            default=date.today)
    published_date = models.DateField(
            blank=True, null=True)

    def publish(self):
        self.published_date = models.DateField(date.today)
        self.save()

    def __str__(self):
        return self.title
