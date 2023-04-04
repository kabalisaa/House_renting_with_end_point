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
