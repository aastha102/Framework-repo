from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_id = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.customer_name