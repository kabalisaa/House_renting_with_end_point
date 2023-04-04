# from django.urls import path, include
# from renting.views import *


# urlpatterns = [
#     # path('home/', ),
# ]

from django.urls import path
from .views import *


urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="LIST_Detail"),
    path("1", PostList.as_view(), name="List"),
    
    path("<int:pk>/", SectorDetail.as_view(), name="LIST_Detail"),
    path("sector", SectorList.as_view(), name="List"),
    
    #urls to access cells
    path("<int:pk>/", CellDetail.as_view(), name="LIST_Detail"),
    path("cell", CellList.as_view(), name="List"),
    
    #urls to create Manager
    path("<int:pk>/", ManagerDetail.as_view(), name="LIST_Detail"),
    path("manager", ManagerList.as_view(), name="List"),
    
      #urls to create Manager
    path("<int:pk>/", LandlordDetail.as_view(), name="LIST_Detail"),
    path("landlord", LandlordList.as_view(), name="List"),
    
    
]
