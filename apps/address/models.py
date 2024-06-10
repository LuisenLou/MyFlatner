from django.db import models

# Create your models here.

class Address(models.Model):
    
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


    via_class = models.CharField (max_length = 20,choices = VIA_CHOICES)

    via_name = models.CharField (max_length = 50 )
    via_number = models.IntegerField ()
    floor = models.CharField(max_length=3, blank=True)
    door = models.CharField(max_length=3, blank=True)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    province_or_state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.via_name}, {self.city}"