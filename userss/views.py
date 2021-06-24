from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from userss.forms import UserLoginForm

# Create your views here.




def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'userss/login.html', context)

def reg(request):
    return render(request, 'userss/register.html')




