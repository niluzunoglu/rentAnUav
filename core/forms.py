from django import forms
from core.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UAVForm(forms.ModelForm):
    class Meta:
        model = UAV
        fields = "__all__"
        
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
        
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
        
class BrandModelForm(forms.ModelForm):
    class Meta:
        model = BrandModel
        fields = "__all__"
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
class SearchForm(forms.Form):
    searchText = forms.CharField(max_length=100)
