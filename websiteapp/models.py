from django.db import models

class Customer_info(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_mail = models.CharField(max_length=100)
    customer_subject =models.CharField(max_length=200)
    customer_messege = models.CharField(max_length=300)

    def __str__(self):
        return self.customer_name
