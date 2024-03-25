from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'bio',
            'profile_image', 
            'facebook', 
            'twitter', 
            'instagram',
            'country',
            'address',
            'phone',
            'website',
            ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter Full Name', 'class': 'prompt srch_explore'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'prompt srch_explore'}),
        }

class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'prompt srch_explore'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'prompt srch_explore'}),
        }
