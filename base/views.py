from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def certification(request):
    return render(request,"certification.html")

def projects(request):
    return render(request ,"projects.html")

def about(request):
    return render(request , "about.html")

def contact(request):
    return render(request , "contact.html")
# Create your views here.
