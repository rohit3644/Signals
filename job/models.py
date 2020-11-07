from django.db import models

# Create your models here.

class Job(models.Model):
    company_name = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    skill = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)
