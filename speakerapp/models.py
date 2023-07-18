from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Speaker(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone=PhoneNumberField(unique = True, null = False, blank = False)
    experience=models.CharField(max_length=100)
    education=models.CharField(max_length=50)
    expertise=models.CharField(max_length=100)
    session_date=models.DateField()
    session_time=models.TimeField()