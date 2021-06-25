from django.urls import path

from userss.views import login, reg, profile

app_name = 'userss'

urlpatterns = [

    path('login/', login, name='log'),
    path('reg/', reg, name='regis'),
    path('profile/', profile, name='prof'),

]