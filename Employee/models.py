from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    FullName=models.CharField(max_length=150)
    Emp_Code=models.CharField(max_length=5)
    Mobile=models.CharField(max_length=15)
    Position=models.ForeignKey(Position,on_delete=models.CASCADE)