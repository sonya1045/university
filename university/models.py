from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100)
    city = models.TextField()
    address = models.CharField(verbose_name='address', max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='static/images/')
    top = models.IntegerField()
    discriptions = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"