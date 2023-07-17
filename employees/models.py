""" Employe Module """
from django.db import models

# Create your models here.
class Employee(models.Model):
    """ Class representing a Employee"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images")
    designation = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """ Column Names"""
        return self.first_name
    
