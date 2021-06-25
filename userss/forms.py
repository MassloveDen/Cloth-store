from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from userss.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder':'Enter pass'}))

    class Meta:
        model = User
        fields = {'username', 'password'}

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter last_name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter login'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}), required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}), required=False)
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

        def __init__(self, *args, **kwargs):
            super(UserChangeForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control py-4'
            self.fields['image'].widget.attrs['class']= 'custom-file-label'



