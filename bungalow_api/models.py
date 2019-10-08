from django.db import models

# Create your models here.
class House(models.Model):

    area_unit = models.CharField(max_length=255)
    bathrooms = models.CharField(max_length=255)
    bedrooms = models.CharField(max_length=255)
    home_size = models.CharField(max_length=255)
    home_type = models.CharField(max_length=255)
    last_sold_date = models.CharField(max_length=255)
    last_sold_price = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    property_size = models.CharField(max_length=255)
    rent_price = models.CharField(max_length=255)
    rentzestimate_amount = models.CharField(max_length=255)
    rentzestimate_last_updated = models.CharField(max_length=255)
    tax_value = models.CharField(max_length=255)
    tax_year = models.CharField(max_length=255)
    year_built = models.CharField(max_length=255)
    zestimate_amount = models.CharField(max_length=255)
    zestimate_last_updated = models.CharField(max_length=255)
    zillow_id = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    def __str__(self):
        return "{}, {}, {}".format(self.address, self.city, self.state)