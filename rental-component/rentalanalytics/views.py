
from django.shortcuts import render, redirect

import requests

from rentalanalytics.rentalAnalyticsScript import rentcastApiCall, insertSampleRentData
 
# import view sets from the REST framework
from rest_framework import viewsets
 
# import the TodoSerializer from the serializer file
from .serializers import RentalAnalysisSerializer
 
# import the Todo model from the models file
from .models import RentalProperties
 
# create a class for the Todo model viewsets
class RentalAnalyticsView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = RentalAnalysisSerializer
 
    # define a variable and populate it
    # with the rental properties list objects
    queryset = RentalProperties.objects.all()


def index(request):
    # api call
    city = 'Miami'
    state = 'FL'
    # rentcastApiCall(city, state)
    properties , averagePricePerSQFT, maxPricePerSQFT, minPricePerSQFT = insertSampleRentData()

    context = {
        'properties': properties,
        'averagePricePerSQFT': averagePricePerSQFT,
        'maxPricePerSQFT': maxPricePerSQFT,
        'minPricePerSQFT': minPricePerSQFT,
    }

    return render(request, 'index.html', context)