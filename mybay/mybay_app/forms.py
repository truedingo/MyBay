from django import forms
from mybay_app.models import Profile, Item
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries import countries
import datetime

CAT_CHOICE = [
    (None, 'None'),
    ('Lifestyle', 'Lifestyle'),
    ('Technology', 'Technology'),
    ('Kitchen', 'Kitchen'),
]

SEARCH_ATTRIBUTES = [
    (None, 'None'),
    ('ascending', 'Ascending'),
    ('descending', 'Descending'),
]


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

class UserDeleteForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}),)
    password_check = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserEditForm(forms.Form):
    new_username = forms.EmailField(label='New email', widget=forms.TextInput(attrs={'class': "form-control"}),)
    new_country = forms.ChoiceField(choices=list(countries), widget=forms.Select(attrs={'class': 'form-control'}))
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'class': "form-control"}),)
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class': "form-control"}),)

class SearchForm(forms.Form):
    category_select = forms.CharField(widget=forms.Select(choices=CAT_CHOICE), required=False, label='')
    my_country = forms.BooleanField(required=False)
    name_select = forms.CharField(widget=forms.Select(choices=SEARCH_ATTRIBUTES), required=False, label="Name")
    price_min = forms.FloatField(required=False)
    price_max = forms.FloatField(required=False)
    date_select = forms.CharField(widget=forms.Select(choices=SEARCH_ATTRIBUTES), required=False)
    after_date = forms.DateField(widget=forms.DateInput(format = '%Y-%m-%d'), required=False)





    