from django.db import models


# Create your models here.

class Contact_form(models.Model):
    class Meta:
        verbose_name = 'Contact_form'
        verbose_name_plural = 'Contact-forms'

    FORM_CHOICES = (
        ('Sugerencia', 'Suggest'),
        ('Duda', 'Query'),
        ('Petición', 'Claim'),
        ('Opinion', 'Opinion'),
    )
    FORM_CHOICES = (
        ('Sugerencia', 'Suggest'),
        ('Duda', 'Query'),
        ('Petición', 'Claim'),
        ('Opinion', 'Opinion'),
    )

    VIA_CHOICES = (
        ('Calle', 'Calle'),
        ('Avenida', 'Avenida'),
        ('Plaza', 'Plaza'),
        ('Carretera', 'Carretera'),
        ('Paseo', 'Paseo'),
        ('Ronda', 'Ronda'),
    )    

    reason =                        models.CharField(max_length = 30 , choices = FORM_CHOICES)

    first_name =                    models.CharField(max_length = 50)
    last_name =                     models.CharField(max_length = 50)
    email =                         models.EmailField(max_length = 100)

    country =                       models.CharField(max_length = 50)
    city =                          models.CharField(max_length=50, null=True, blank=True)
    region =                        models.CharField(max_length=50, null=True, blank=True)
    via =                           models.CharField(max_length = 30 , choices = VIA_CHOICES, null=True, blank=True)
    address_name =                  models.CharField(max_length=100, null=True, blank=True)
    postal_code =                   models.CharField(max_length = 20, null=True, blank=True)

    description =                   models.TextField(max_length = 1000)

    created_at =                    models.DateTimeField(auto_now_add=True)
    ip_address =                    models.CharField(max_length = 45)

    def __str__(self):
        return self.title



