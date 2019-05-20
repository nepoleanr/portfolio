from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        stringified_body = str(self.body)
        return stringified_body[:100] + "..."


    def pub_date_pretty(self):
        return self.published_date.strftime('%b %e %Y')
    
    def __str__(self):
        return self.title