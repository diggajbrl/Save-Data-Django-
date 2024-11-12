from django.db import models

# Create your models here.

class Myform (models.Model) :

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    my_email = models.CharField(max_length=70, unique=True)