from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('houses', views.HouseView)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-csv/', views.house_upload, name="house_upload"),
]