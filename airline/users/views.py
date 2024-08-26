from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# main login page

def index(request):
    # if no user is signed in, return to the login page
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # check if username and password are correct, reutrning User Object
        user = authenticate(request, username=username, password=password)

        # if user object is returned, log in and route to index page
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        # otherwise login pgae iwht new context
        else:
            return render(request, "users/login.html", {
                "message " : "Invalid Credentials"
            })
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
                "message": "Logged Out"
            })