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
]
