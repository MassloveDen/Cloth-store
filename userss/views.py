from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'userss/login.html')

def reg(request):
    return render(request, 'userss/register.html')




