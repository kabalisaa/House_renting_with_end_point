# from django.shortcuts import render
# from renting.models import *


# # Create your views here.
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.
# posts/views.py

class PostList(generics.ListCreateAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    

class SectorList(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    
class SectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    

#here is the URLS FOR CELLS

class CellList(generics.ListCreateAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    
class CellDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer

#here is the URLS FOR Manager
class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    
class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

#here is the URLS FOR Landlord
class LandlordList(generics.ListCreateAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer
    
class LandlordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer
    
#here is the URLS FOR PropertyType 
class PropertyTypeList(generics.ListCreateAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    
class PropertyTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    
#here is the URLS FOR PropertyType 
class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
#here is the URLS FOR PropertyImages
class PropertyImagesList(generics.ListCreateAPIView):
    queryset = PropertyImages.objects.all()
    serializer_class = PropertyImagesSerializer
    
class PropertyImagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyImages.objects.all()
    serializer_class = PropertyImagesSerializer

#here is the URLS FOR PublishingPayment
class PublishingPaymentList(generics.ListCreateAPIView):
    queryset = PublishingPayment.objects.all()
    serializer_class = PublishingPaymentSerializer
    
class PublishingPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PublishingPayment.objects.all()
    serializer_class = PublishingPaymentSerializer
