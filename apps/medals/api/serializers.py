from rest_framework import serializers 
from ..models import Country,Sport,Medal


class CountrySerializers(serializers.ModelSerializer): 
   class Meta: 
     model = Country
     fields = '__all__'

class SportSerializers(serializers.ModelSerializer): 
   class Meta: 
     model = Sport
     fields = '__all__'

class MedalSerializers(serializers.ModelSerializer): 
   class Meta: 
     model = Medal
     fields = '__all__'