from django.db import models
from apps.account.models import Account
from apps.flat.models import Flat

# Create your models here.

class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    STATUS_CHOICES = (
        ('Pendiente', 'Pending'),
        ('Terminado', 'Finished'),
        ('Aplazado', 'Posponed'),
    )
    title = models.CharField(max_length = 30, unique = True)
    status = models.CharField(max_length=15, choices = STATUS_CHOICES)
    task_date = models.DateField (auto_now_add = True)
    task_limit_date = models.DateField ()
    assigned_to = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tasks')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='tasks')

    def __str__ (self):
        return self.title
    
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.task_limit_date < self.task_date:
            raise ValidationError('The limit date cannot be earlier than the task date.')
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
