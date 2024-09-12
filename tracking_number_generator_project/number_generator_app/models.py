from django.db import models

import random
import string

# Create your models here.
class CreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    class Meta:
        abstract = True

class TrackingDetail(CreatedModel):
    origin_country_id = models.CharField(max_length=5, blank=False)
    destination_country_id = models.CharField(max_length=5, blank=False)
    weight = models.DecimalField(max_digits=10, decimal_places=3, blank=False)
    
    customer_id = models.UUIDField(blank=False)
    customer_name = models.CharField(max_length=100, blank=False)
    customer_slug = models.SlugField(max_length=100, blank=False)


def generate_unique_string(length=16):
    characters = string.ascii_uppercase + string.digits + string.ascii_lowercase

    while True:
        random_string = ''.join(random.choices(characters, k=length))
        if not TrackingSubDetail.objects.only('tracking_number').filter(tracking_number=random_string).exists():
            return random_string.upper()
        
class TrackingSubDetail(CreatedModel):
    tracking_detail = models.OneToOneField('number_generator_app.TrackingDetail', on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=16, default=generate_unique_string)