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

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "user",
        "gender",
        "province",
        "phone_number",
        "district",
        "sector",
        
        )
        model = Manager


class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "user",
        "gender",
        "province",
        "phone_number",
        "district",
        "sector",
        "cell",
        
        )
        model = Landlord


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "type_name",
        
        )
        model = PropertyType   

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "landlord",
        "property_type",
        "title",
        "description",
        "bedrooms",
        "bathrooms",
        "is_furnished",
        "floors",
        "plot_size",
        "renting_price",
        "status",
        "pub_date",
        "created_date",
        "province",
        "district",
        "sector",
        "cell",
        "street",   
        
        )
        model = Property   


class PropertyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "property",
        "property_image",
        
        )
        model = PropertyImages   

class PublishingPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "property",
        "landlord",
        "payment_amount",
        "payment_method",
        "created_date", 
        )
        model = PublishingPayment   