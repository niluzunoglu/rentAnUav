from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('list',views.listUavs,name='listUavs'),
    path('update/<uavId>',views.updateUav,name='updateUavs'),
    path('delete/<uavId>',views.deleteUav,name='deleteUav'),
    path('addUav',views.createUav,name='addUav')

]