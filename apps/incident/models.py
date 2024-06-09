from django.db import models
from apps.account.models import Account
from apps.flat.models import Flat 

# Create your models here.

class Incident(models.Model):
    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'


    flat = models.ForeignKey(Flat, on_delete = models.CASCADE)
    applicant = models.ForeignKey (Account, on_delete= models.CASCADE)
    receiver = models.ForeignKey (Account, on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('Aceptado', 'Accepted'),
        ('Rechazada', 'Rejected'),
        ('Pendiente', 'Pending'),
    )

    incident_status = models.CharField (max_length = 3, choices = STATUS_CHOICES)
    incident_date = models.DateField(auto_now_add = True)

