from django.db import models

# Create your models here.

class Address(models.Model):
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
    
    VIA_CHOICES = (
            ('CALLE', 'Calle'),
            ('AVENIDA', 'Avenida'),
            ('PLAZA', 'Plaza'),
            ('CAMINO', 'Camino'),
            ('PASEO', 'Paseo'),
            ('CARRETERA', 'Carretera'),
            ('AUTOPISTA', 'Autopista'),
            ('RAMBLA', 'Rambla'),
            ('TRAVESÍA', 'Travesía'),
            ('GLORIETA', 'Glorieta'),
            ('RONDA', 'Ronda'),
            ('CARRERA', 'Carrera'),
            ('VÍA', 'Vía'),
            ('PASAJE', 'Pasaje'),
            ('BULEVAR', 'Bulevar'),
        )


    via_class =                 models.CharField (max_length = 20,choices = VIA_CHOICES)

    via_name =                  models.CharField (max_length = 50 )
    via_number =                models.IntegerField (blank=True, null=True)
    floor =                     models.CharField(max_length=5, blank=True)
    door =                      models.CharField(max_length=5, blank=True)
    postal_code =               models.CharField(max_length=20)
    
    city =                      models.CharField(max_length=50)
    province_or_state =         models.CharField(max_length=50)
    country =                   models.CharField(max_length=50)


    def __str__(self):
        return f"{self.via_name}, {self.city}"