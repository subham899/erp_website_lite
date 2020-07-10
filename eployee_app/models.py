from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    Full_name = models.CharField(max_length=100)
    Erp_code = models.CharField(max_length=100)
    Mobile_no = models.CharField(max_length=11)
    Position = models.ForeignKey(Position, on_delete=models.CASCADE)
