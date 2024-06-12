from django.db import models
from apps.account.models import Account
from apps.flat.models import Flat 

# Create your models here.

class Incident(models.Model):
    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'

    STATUS_CHOICES = (
        ('Aceptado', 'Accepted'),
        ('Rechazada', 'Rejected'),
        ('Pendiente', 'Pending'),
    )

    title =                 models.CharField(max_length = 50, default='Temporary Default Title')
    flat =                  models.ForeignKey(Flat, on_delete = models.CASCADE)
    applicant =             models.ForeignKey (Account, on_delete= models.CASCADE, related_name='applied_incidents')
    receiver =              models.ForeignKey (Account, on_delete=models.CASCADE, related_name='received_incidents')

    incident_status =       models.CharField (max_length = 20, default='Pendiente', choices = STATUS_CHOICES)
    incident_date =         models.DateField(auto_now_add = True)

    description =           models.TextField(max_length = 255, blank=True, null=True)

