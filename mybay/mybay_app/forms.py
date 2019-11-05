from django import forms
from mybay_app.models import Profile, Item
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries import countries


class SignUpForm(forms.ModelForm):
    username = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': "form-control"}))
    password_check = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'password', 'password_check')
        widgets = {'password': forms.PasswordInput(attrs={'class': 'form-control'})}
    
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        pass1 = cleaned_data.get('password_check')
        pass2 = cleaned_data.get('password')
        if pass1 != pass2:
            raise forms.ValidationError("The two password fields must match.")
        return cleaned_data

class ProfileForm(forms.ModelForm):
    user_country = forms.ChoiceField(choices=list(countries), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        labels = {'user_country': 'Country'}
        fields = ('user_country',)

class LoginForm(forms.Form):
    username = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': "form-control"}),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}),)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_name', 'item_category', 'item_price', 'item_pic',)
    