from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import GroceryItem
from django.http import HttpResponse




@login_required
def home(request):

    item_list = GroceryItem.objects.filter(item_owner=request.user)
    return render(request,'pages/index.html',{'item_list':item_list})

def login_view(request):
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_name = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=user_name,password=password)
            if user is not None:
                auth.login(request,user)
        
                return redirect('home-page')
            else:
                messages.error(request,'Invalid credentials')
                return redirect('login-page')
        
        else:
            return render(request,'pages/login.html')
    else:
        return redirect('home-page')

def reg_view(request):

    if not request.user.is_authenticated:
        if request.method == 'POST':

            user_name = request.POST['username']
            email = request.POST['email']
            full_name = request.POST['fullname']
            password = request.POST['password']
            c_password = request.POST['password_confirm']

            if password == c_password:
                if User.objects.filter(username=user_name).exists():
                    messages.error(request,"Username is already taken..")
                    return redirect('reg-page')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request,'Email is being used')
                        return redirect('reg-page')
                    else:
                        # registration logic is good here
                        user = User.objects.create_user(username=user_name,password=password,email=email,first_name=full_name)
                        user.save()
                        send_mail('Greetings form Grocery Bag',f'Thank you {full_name} for register with us',
                        'tutbuddy56@gmail.com',[email],fail_silently=False,)
                        messages.success(request,'You are registered and can log in')
                        return redirect('login-page')
            else:
                messages.error(request,'Password do not match. please check your password')
                return redirect('reg-page')
        else:
            return render(request,'pages/registration.html')
    else:
        return redirect('home-page')


    


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('login-page')

@login_required
def add_item(request):

    if request.method == 'POST':
        grocery_item = GroceryItem.objects.create(item_owner=request.user,item_name=request.POST['item_name'],item_qty=request.POST['item_qty'],item_status=request.POST['item_status'],item_date=request.POST['item_date'])
        messages.success(request,'Item Added Successfully')
        return redirect('add-item')
    else:
        return render(request,'pages/add.html')

def update_item(request,item_id):
    
    single_item = GroceryItem.objects.get(pk=item_id)
    return render(request,'pages/update.html',{'item_data' : single_item})

    
@login_required
def update_data(request):

    if(GroceryItem.objects.filter(id = request.POST['item_id']).update(item_name=request.POST['item_name'],item_qty=request.POST['item_qty'],item_status=request.POST['item_status'],item_date=request.POST['item_date'])):
        return HttpResponse("ok")
    else:
        return HttpResponse("err")
@login_required
def delete_item(request,item_id):

    test = GroceryItem.objects.filter(id=item_id).delete()
    if test[0] > 0:
        return HttpResponse("ok")
    else:
        return HttpResponse("error")

@login_required
def search_item(request):
    
    filtered_data = GroceryItem.objects.filter(item_date=request.GET['item-date'],item_owner = request.user)
    return render(request,'pages/index.html',{'item_list':filtered_data})
    

  


   

    
   
    



       
   
