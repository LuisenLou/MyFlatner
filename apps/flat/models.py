from django.db import models
import requests
from apps.account.models import Account
from apps.address.models import Address
# Create your models here.

class Flat(models.Model):
    class Meta:
        verbose_name = 'Flat'
        verbose_name_plural = 'Flats'


    landlord = models.ForeignKey(Account, on_delete = models.CASCADE, related_name= 'owned_flats')

    title = models.CharField(max_length = 255, unique=True )
    description = models.TextField(max_length = 255)

    published = models.DateField(auto_now_add = True)
    num_rooms = models.IntegerField(default = 0, blank=True)
    num_bathrooms = models.IntegerField(default = 1, blank=True)

    area = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


    #Google Maps 
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    photos = models.ImageField(upload_to='/media/', blank=True, null=True)

    views = models.IntegerField(default = 0, blank = True)

    def get_view_count(self):
        views = ViewCount.objects.filter(Flat = self).count()
        return views


    def save(self, *args, **kwargs):
        if self.address:
            lat, lng = geocode_address(self.address)
            if lat and lng:
                self.latitude = lat
                self.longitude = lng
        super().save(*args, **kwargs)


def geocode_address(address):
    params = {
        'address': address,
        'key': 'MY_API_KEY' 
    }
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    
    try:
        # Realizar la solicitud GET a la API de Geocodificación
        response = requests.get(url, params=params)
        data = response.json()

        # Verificar si la solicitud fue exitosa y si se obtuvieron resultados
        if response.status_code == 200 and data['status'] == 'OK':
            # Extraer las coordenadas de latitud y longitud de la respuesta
            location = data['results'][0]['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            return lat, lng
    except Exception as e:
        print(f"Error al obtener las coordenadas para la dirección '{address}': {e}")

    return None, None


class ViewCount(models.Model):
    flat = models.ForeignKey(Flat, related_name = 'room_view_count', on_delete = models.CASCADE)
    ip_address = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.ip_address}'
