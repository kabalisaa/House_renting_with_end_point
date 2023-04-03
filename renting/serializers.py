from rest_framework import serializers
from renting.models import *

# create serializers here

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "province_name",
        
        )
        model = Province
        

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "district_name",
        "province",
        
        )
        model = District  
    
class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "sector_name",
        "district",
        
        )
        model = Sector
        
class CellSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "cell_name",
        "sector",
        
        )
        model = Cell

    