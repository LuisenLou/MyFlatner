from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        email =         self.normalize_email(email)
        user =          self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email,password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

def account_image_directory(instance, filename):
    return 'account/{0}/{1}'.format(instance.title, filename)


class Account(AbstractBaseUser, PermissionsMixin):


    GENRE_CHOICES = (
        ('M', 'Masculino'),
        ('W', 'Femenino'),
        ('N', 'Prefiero no decirlo'),
    )
        
    OCUPATION_CHOICES = (
        ('Estudiante', 'Student'),
        ('Trabajador', 'Worker'),
    )

    ROLE_CHOICES = (
        ('Inquilino', 'Tenant'),
        ('Propietario', 'Landlord'),
    )
    

    email =                     models.EmailField(max_length=255, unique = True)
    password =                  models.CharField(max_length=128, blank=True, null=True)

    username =                  models.CharField(max_length = 20, unique = True )

    first_name =                models.CharField(max_length=255, null = True, blank = True)
    last_name =                 models.CharField(max_length=255, null = True, blank = True)
    birth_date =                models.DateField(null = True, blank = True)
    genre =                     models.CharField (max_length = 1, choices = GENRE_CHOICES)
    
    country =                   models.CharField(max_length=50, null = True, blank = True)
    province_or_state =         models.CharField(max_length=50, null = True, blank = True)
    city =                      models.CharField(max_length=50, null = True, blank = True)
    #Probably create the Ocupation Model to add more.
    ocupation =                 models.CharField(max_length=15,choices = OCUPATION_CHOICES, null = True, blank = True)

    profile_photo =             models.ImageField(upload_to='media/', blank=True, null=True)

    description =               models.TextField(max_length = 1000, blank=True, null=True)

    role =                      models.CharField(max_length = 20, choices = ROLE_CHOICES)
    #To add : interests

    is_active =                 models.BooleanField(default=True)
    is_staff =                  models.BooleanField(default=False)

    is_editor =                 models.BooleanField(default=False)

    objects =                   UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

