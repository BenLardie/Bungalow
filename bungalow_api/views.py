from django.shortcuts import render
from rest_framework import viewsets
from .models import House
from .serializer import HouseSerializers
import csv, io
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

def house_upload(request):
    template = 'house_upload.html'

    promt = {
        'order': 'Order of the CSV should be'
    }

    if request.method == 'GET':
        return render(request, template, promt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = House.objects.update_or_create(
        area_unit = column[0],
        bathrooms = column[1],
        bedrooms = column[2],
        home_size = column[3],
        home_type = column[4],
        last_sold_date = column[5],
        last_sold_price = column[6],
        link = column[7],
        price = column[8],
        property_size = column[9],
        rent_price = column[10],
        rentzestimate_amount = column[11],
        rentzestimate_last_updated = column[12],
        tax_value = column[13],
        tax_year = column[14],
        year_built = column[15],
        zestimate_amount = column[16],
        zestimate_last_updated = column[17],
        zillow_id = column[18],
        address = column[19],
        city = column[20],
        state = column[21],
        zipcode = column[22]
        )
    context = {}
    return render(request, template, context)

class HouseView(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializers


