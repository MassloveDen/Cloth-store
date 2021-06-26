from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from userss.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket
from django.contrib.auth.decorators import login_required
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
            messages.success(request, 'Registration success!')
            return HttpResponseRedirect(reverse('userss:log'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'userss/register.html', context)

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userss:prof'))
    else:
        form = UserProfileForm(instance=user)


    baskets = Basket.objects.filter(user=user)
    total_quantity = sum(basket.quantity for basket in baskets)
    total_sum = sum(basket.sum() for basket in baskets)


    context = {'form':form,
               'baskets': baskets,
               'total_quantity': total_quantity,
               'total_sum': total_sum,
               }
    return render(request, 'userss/myprofile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))
