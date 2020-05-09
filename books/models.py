from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    name = models.TextField(max_length=256)
    author = models.TextField(max_length=256)
    available = models.BooleanField(default=False)
    copies = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:detail',kwargs={'pk':self.pk})
    class Meta:
        ordering = ['name']
