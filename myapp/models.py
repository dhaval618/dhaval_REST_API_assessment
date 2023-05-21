from django.db import models

# Create your models here.
class snippet(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=150)
    linenos = models.BooleanField()
    language = models.CharField(max_length=100)
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.title
