from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=256)
    roll_no = models.IntegerField()
    branch = models.CharField(max_length=5)
    sem = models.IntegerField(default=1)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('students:detail',kwargs={'pk':self.pk})
