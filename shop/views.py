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


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(username, pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username and Password is Incorrect!")
    return render(request, 'shop/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('LoginPage')
def index(request):
    product_objects = Product.objects.all()

    #search code
    #code file
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(category__icontains=item_name)

    # paginator code
    paginator = Paginator(product_objects, 8)
    page = request.GET.get("page")
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})

def detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})


def about(request):
    return render(request, 'shop/about.html')
