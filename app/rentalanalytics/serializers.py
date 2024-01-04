
# import serializers from the REST framework
from rest_framework import serializers
 
# import the todo data model
from .models import RentalProperties
 
# create a serializer class
class RentalAnalysisSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = RentalProperties
        fields = ('id', 'address','price','size', 'pricePerSqft')
