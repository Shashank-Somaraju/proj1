from django.shortcuts import render , redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        #messages.error(request,'hi')
        if User.objects.filter(username=username).exists():
            user=auth.authenticate(username=username , password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,'Successfully logged in')
                return redirect('index')
            else:
                messages.error(request,'PLease neter correct password')
                return redirect('login')
        else:
            messages.error(request,'Please register befor logging in')
            return redirect('login')   
    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password != password2 :
            messages.error(request,'passowrds dont match')
            return redirect('register')    
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already taken')
            print("hi")
            return redirect('register')
        user=User.objects.create_user(username=username , password=password ,email = email,first_name=first_name,last_name=last_name)
        user.save()
        print("success")
        messages.success(request,'You are now registered and can log in')
        return redirect('login')
    return render(request,'accounts/register.html')

def logout(request):
    auth.logout(request)
    messages.success(request,'You are succesfully logged out')
    return redirect('index')

def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  print(user_contacts.count())
  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)