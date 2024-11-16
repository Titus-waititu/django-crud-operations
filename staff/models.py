from django.db import models

# Create your models here.
class Staff(models.Model):
    image = models.ImageField(upload_to='staff_images')
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.fname