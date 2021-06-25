from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from userss.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userss:log'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'userss/register.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userss:prof'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form':form}
    return render(request, 'userss/myprofile.html', context)


