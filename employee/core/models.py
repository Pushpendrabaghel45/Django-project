from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    Join_date = models.DateField()

    def __str__(self):
        return self.name