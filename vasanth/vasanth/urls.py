from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofasquareprism/',views.prismarea,name="areaofasquareprism"),
    path('',views.prismarea,name="areaofasquareprismroot")
]