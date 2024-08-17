from rest_framework import viewsets 
from .serializers import CountrySerializers, SportSerializers, MedalSerializers
from ..models import Country,Sport,Medal 

class CountryViewsets(viewsets.ModelViewSet): 
    serializer_class = CountrySerializers
    queryset = Country.objects.all()

class SportViewsets(viewsets.ModelViewSet):  
    serializer_class = SportSerializers
    queryset = Sport.objects.all()

class MedalViewsets(viewsets.ModelViewSet):  
    serializer_class = MedalSerializers
    queryset = Medal.objects.all()