from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from core.models import UAV
from core.forms import *
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q 

def sign_up(request):
   
    if request.method == 'POST':
        
        form = RegisterForm(request.POST) 
        
        if form.is_valid():
            
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'You have signed up successfully.')
            
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            return redirect('/list')
        
        else:
            messages.error(request,"Form is not valid.")
            return render(request, 'registration/signup.html', {'form': form})
        
    form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})    

def homePage(request):
    
    if request.user.is_authenticated:
        return redirect('listUavs')
    
    else:
        return render(request,"core/homePage.html")

def listUavs(request):
    
    rentedFlag = False
    uavList = UAV.objects.all()
    return render(request,"core/listUavs.html",{"uavList":uavList,"rentedFlag":rentedFlag})

def listAvailableUavs(request):
    
    rentedFlag = True
    uavList = UAV.objects.filter(isRented=False).all()
    return render(request,"core/listAvailableUavs.html",{"uavList":uavList,"rentedFlag":rentedFlag})

def updateUav(request,uavId):
    
    if request.method == "POST":
        
        uav = UAV.objects.get(id=uavId)  
        form = UAVForm(request.POST, instance = uav)
          
        if form.is_valid():  
            
            try:
                form.save()  
                messages.success(request,'Info updated successfully')
                return redirect('/list')  

            except Exception as e:
                messages.error(request,e)
                return redirect('/list')
        else:
            messages.error(request,"Form is not valid. Try again")
            return redirect("/list")
        
    else:
        uav = UAV.objects.get(id=uavId)
        uavForm = UAVForm(instance=uav)
        return render(request,"core/edit.html",{"uav":uav, "uavForm":uavForm})
    
def createUav(request):
    
    if request.method == "POST":
         
        form = UAVForm(request.POST)  
        
        if form.is_valid():  
                
            try:  
                form.save()  
                messages.success(request,"UAV created successfully.")
                return redirect('/list')  
            except Exception as e:  
                messages.error(request,e)
                return redirect('/list')
        
        else:
            messages.error(request,"Form is not valid. Try again")
            return redirect("/list")
        
    else:
        uavForm = UAVForm()
        return render(request,"core/createUav.html",{"uavForm":uavForm})

def deleteUav(request,uavId):
    
    try:
        deleted_item = UAV.objects.get(id=uavId).delete()
        messages.success(request,"UAV deleted successfully")
        return redirect('/list')
        
    except Exception as e :
        messages.error(request,e)
        return redirect('/list')
        
def addCategory(request):
    
    if request.method == "POST":
        
        form = CategoryForm(request.POST)  
        
        if form.is_valid():  
            
            try:  
                form.save()  
                messages.success(request, 'Category added.')
                return redirect('/list')  
            
            except Exception as e:  
                messages.error(request, e)
                return redirect('/list')    
            
        else:
            messages.error(request, 'Form is not valid. Try again later')
            return redirect('/list') 
            
    else:
        
        form = CategoryForm()
        return render(request,"core/addCategory.html",{"categoryForm":form})
    
def addBrand(request):
    
    if request.method == "POST":
        
        form = BrandForm(request.POST)  
        
        if form.is_valid():  
            
            try:  
                form.save()  
                messages.success(request, 'Brand added.')
                return redirect('/list')
            
            except Exception as e:  
                messages.error(request, e)
                return redirect('/list')    
                   
        else:
            messages.error(request, 'Form is not valid. Try again later')
            return redirect('/list') 
        
    else:
        
        form = BrandForm()
        return render(request,"core/addBrand.html",{"brandForm":form})
    
def addModel(request):
    
    if request.method == "POST":
        
        form = BrandModelForm(request.POST)  
        
        if form.is_valid():  
            try:  
                form.save()  
                messages.success(request, 'Model added.')
                return redirect('/list')
            
            except Exception as e:  
                messages.error(request, e)
                return redirect('/list')    
            
        else:
            messages.error(request, 'Form is not valid. Try again later')
            return redirect('/list') 
        
    else:
        
        form = BrandModelForm()
        return render(request,"core/addModel.html",{"brandModelForm":form})
    
def search(request):
    
    if request.method == "POST":
        
        search = request.POST["searchText"]
        
        result = UAV.objects.filter(Q(name__icontains=search) | Q(brand__brandName__icontains=search) | Q(brandModel__modelName__icontains=search) | Q(category__categoryName__icontains=search)).all()
        print(search)
        print(result)
        
        if list(result) == []:
            messages.error(request, 'UAV not found') 
            return redirect('/list')

        messages.success(request,"Search results fetched")
        return render(request,"core/listUavs.html",{"uavList":result})
    
    else:
        return redirect('/list')
        
def rent(request,id):
    
    if request.user.is_authenticated:
        
        user = User.objects.get(username = request.user.username)
    
        uavObject = UAV.objects.get(id=id)
        
        if uavObject.isRented == False:
            
            operation = RentOperations(uav=uavObject,user=user)
            
            uavObject.isRented = True
            uavObject.save()
            
            messages.success(request,'UAV rented successfully')
            return redirect('/list')
        
        else:
            messages.error(request,'This UAV has rented already. Try again with another.')
            return redirect('/list')        
    
        
def detail(request,id):
    
    try:
        uav=UAV.objects.get(id=id)
        
    except Exception as e:
        messages.error(request,e)
        return redirect('/list')
    
    return render(request,"core/detailedInfoPage.html",{"uav":uav})