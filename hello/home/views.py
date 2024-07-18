from django.shortcuts import render,redirect,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    # HttpResponse("Hello Muhammad Awais to redirect the Home Page")
    # if request.user.is_anonymous:
    #     return redirect("login.html")
    return render(request,'home.html')
def home(request):
    # HttpResponse("Hello Muhammad Awais to redirect the Home Page")
    if request.user.is_anonymous:
        return redirect("login.html")
    return render(request,'home.html')
def Blog(request):
    # HttpResponse("Hello Muhammad Awais to redirect the Home Page")
    if request.user.is_anonymous:
        return redirect("login.html")
    return render(request,'Blog.html')
def hosting(request):
    # HttpResponse("Hello Muhammad Awais to redirect the Home Page")
    if request.user.is_anonymous:
        return redirect("login.html")
    return render(request,'hosting.html')
def Discount(request):
    # HttpResponse("Hello Muhammad Awais to redirect the Home Page")
    if request.user.is_anonymous:
        return redirect("login.html")
    return render(request,'Discount.html')
def contact(request):
    # HttpResponse("Hello Muhammad Awais to redirect the Home Page")
    if request.user.is_anonymous:
        return redirect("login.html")
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        textarea = request.POST.get('textarea')
        contact = Contact(name=name , email=email , subject=subject , textarea=textarea , date=datetime.today())
        contact.save()
        

    return render(request,'contact.html')
def Gear(request):
    # HttpResponse("Hello Muhammad Awais to redirect the Home Page")
    if request.user.is_anonymous:
        return redirect("login.html")
    return render(request,'Gear.html')
def loginUser(request):
    # HttpResponse("Hello Muhammad Awais to redirect the Home Page")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return redirect("login.html")
    return render(request,'login.html')
def logoutUser(request):
    # HttpResponse("Hello Muhammad Awais to redirect the Home Page")
    logout(request)
    if request.user.is_anonymous:
        return redirect("login.html")
    return render(request,'logout.html')















