from django.db import models

# Create your models here.  pip install psycopg2-binary
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
