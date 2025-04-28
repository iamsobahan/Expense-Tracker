from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists using try-except
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Username does not exist. please register first")
            return redirect('login')

        # Now authenticate using the user object
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

        # Login the user if authentication is successful
        login(request, user_obj)
        messages.success(request, "login successfully")
        return redirect('expense')  # Redirect to home or dashboard page
        
    return render(request, 'login.html')



def register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        cpassword = request.POST.get('cpassword')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')
        

        if not username or not email or not password or not cpassword:
            messages.error(request, "All fields are required.")
            return redirect('register')   # <--- important! stop here
        
        if password != cpassword:
            messages.error(request, "Passwords do not match.")
            return redirect('register')   # <--- important! stop here

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Successfully registered! Please login.")
        return redirect('login')   # <--- after success, redirect to login page
    
    context = {
        'username' : request.POST.get('username'),
        'email' : request.POST.get('email'),
        }

    return render(request, 'register.html', context)


def logout_page(request) : 
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('login')