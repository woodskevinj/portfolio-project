from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, null=True)
    pub_date = models.DateTimeField(null=True)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', null=True)


    # change admin view to show actual title not "blog object"
    def __str__(self):
        return self.title

    # create custom method to show preview only for body

    def summary(self):
        return self.body[:100]

    # create custom method to show date only

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
