from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.CharField(max_length=100)
    name = models.CharField(  max_length=100)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    country = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.customer_name
