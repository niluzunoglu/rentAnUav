from django import forms
from core.models import UAV

class UAVForm(forms.ModelForm):
    
    class Meta:
        model = UAV
        fields = "__all__"