from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^',include("smarthome.urls",namespace="SmartHome")),
    re_path(r'^api_auth/',include('rest_framework.urls',namespace="rest_framework")),
]