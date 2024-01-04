
from django.shortcuts import render, redirect

import requests

from rentalanalytics.rentalAnalyticsScript import rentcastApiCall, insertSampleRentData
 
# import view sets from the REST framework
from rest_framework import viewsets
 
# import the TodoSerializer from the serializer file
from .serializers import RentalAnalysisSerializer
 
# import the Todo model from the models file
from .models import RentalProperties

# Import form from input
from .forms import CityStateForm

# create a class for the Todo model viewsets
class RentalAnalyticsView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = RentalAnalysisSerializer
 
    # define a variable and populate it
    # with the rental properties list objects
    queryset = RentalProperties.objects.all()


def index(request):
    # TODO: api call must be done separately to prevent overspending
    
    if request.method == 'POST':
        form = CityStateForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            rentcastApiCall(city, state)
            properties , averagePricePerSQFT, maxPricePerSQFT, minPricePerSQFT = insertSampleRentData()
        
        #Check if properties is empty
        if properties and 'city' in properties[0]:
            cityInput = properties[0]['city']
            stateInput = properties[0]['state']
        else:
            cityInput = None
            stateInput = None

    else:
        form = None
        properties , averagePricePerSQFT, maxPricePerSQFT, minPricePerSQFT = insertSampleRentData()
        
        # Check if properties is empty/ Extract values from sample
        if properties and 'city' in properties[0]:
            cityInput = properties[0]['city']
            stateInput = properties[0]['state']
        else:
            cityInput = None
            stateInput = None

    context = {
        'form': form,
        'properties': properties,
        'city':cityInput,
        'state':stateInput,
        'averagePricePerSQFT': averagePricePerSQFT,
        'maxPricePerSQFT': maxPricePerSQFT,
        'minPricePerSQFT': minPricePerSQFT,
    }

    return render(request, 'index.html', context)