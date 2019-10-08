from rest_framework import serializers
from .models import House

class HouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('area_unit', 'bathrooms', 'bedrooms', 'home_size', 'home_type', 'last_sold_date', 'last_sold_price', 'link', 'price', 'property_size', 'rent_price', 'rentzestimate_amount', 'rentzestimate_last_updated', 'tax_value', 'tax_year', 'year_built', 'zestimate_amount', 'zestimate_last_updated', 'zillow_id', 'address', 'city', 'state', 'zipcode')