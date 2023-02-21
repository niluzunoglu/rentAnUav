from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from core.models import UAV
from core.forms import UAVForm

def homePage(request):
    
    if User is not None:
        return redirect('listUavs')
    
    else:
        return render(request,"core/homePage.html")

def listUavs(request):
    
    uavList = UAV.objects.all()
    return render(request,"core/listUavs.html",{"uavList":uavList})

def updateUav(request,uavId):
    return render(request,"core/error.html",{"error":"ERROR in UPDATE"})

def createUav(request):
    
    if request.method == "POST":
        cleaned_data = request.data.get("KEY")
        return render(request,"core/error.html",{"error":"CREATE UAV "})

    else:
        uavForm = UAVForm()
        return render(request,"core/createUav.html",{"uavForm":uavForm})

def deleteUav(request,uavId):
    
    try:
        deleted_item = UAV.objects.get(id=uavId).delete()
        return render(request,"core/error.html",{"error":"ERROR in DELETE UAV"})
        
    except:
        return render(request,"core/error.html",{"error":"ERROR EXCEPT İN DELETE UAV"})

    
    
