from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Models):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    GENRE_CHOICES:{
        ('M', 'Masculino'),
        ('W', 'Femenino'),
        ('N', 'Prefiero no decirlo'),
    }

    OCUPATION_CHOICES = (
        ('Estudiante', 'Student'),
        ('Trabajador', 'Worker'),
    )
    

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    username = models.CharField(max_length = 20, unique = True )

    birth_date = models.DateField()
    genre = models.CharField (max_length = 1, choices = GENRE_CHOICES)
    country = models.CharField(max_length=100)
    province_or_state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    #Probably create the Ocupation Model to add more.
    ocupation = models.CharField(choices = OCUPATION_CHOICES)

    profile_photo = models.ImageField(upload_to='/media/', blank=True, null=True)

    description = models.TextField(max_lenght = 255, blank=True, null=True)

    ROLE_CHOICES = (
        ('Inquilino', 'Tenant'),
        ('Propietario', 'Landlord'),
    )

    role = models.CharField(max_length = 10, choices = ROLE_CHOICES)
    #To add : interests


    def __str__(self):
        return self

