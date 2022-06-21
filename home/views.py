from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from home.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        if password:
            pass
        else:
            return render(request, 'auth-failed.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            user = User()
            user.name = name
            user.email = email
            user.phone = phone
            user.password = make_password(password)
            user.save()
            return redirect(home)
        else:
            return render(request, 'auth-failed.html')