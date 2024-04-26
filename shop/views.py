from .models import Product, Order
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def SignUpPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password anc confirm password are not same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            # return HttpResponse("User has been create successfully")
            return redirect('LoginPage')

        # print(uname, email, pass1, pass2)

    return render(request, 'shop/signup.html')

