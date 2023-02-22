from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('list',views.listUavs,name='listUavs'),
    path('listAvailable',views.listAvailableUavs,name='listAvailable'),
    path('update/<uavId>',views.updateUav,name='updateUav'),
    path('delete/<uavId>',views.deleteUav,name='deleteUav'),
    path('addUav',views.createUav,name='addUav'),
    path('signUp', views.sign_up, name="signUp"),
    
    path('addCategory',views.addCategory,name="addCategory"),
    path('addBrandModel',views.addModel,name="addBrandModel"),
    path('addBrand',views.addBrand,name="addBrand"),
    
    path('search',views.search,name="search")


]