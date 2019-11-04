from django import forms
from mybay_app.models import Profile
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    username = forms.EmailField(label="Email")
    password_check = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'password_check')
        widgets = {'password': forms.PasswordInput()}
    
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        pass1 = cleaned_data.get('password_check')
        pass2 = cleaned_data.get('password')
        if pass1 != pass2:
            raise forms.ValidationError("The two password fields must match.")
        return cleaned_data

class ProfileForm(forms.ModelForm):
        class Meta:
            model = Profile
            labels = {'user_country': 'Country'}
            fields = ('user_country',)


'''
class SignUpForm(forms.ModelForm):
    user_pass_check = forms.CharField(label="Password confirmation", widget=forms.PasswordInput())
    class Meta:
        model = Profile
        fields = ["user_email", "user_country", "user_pass"]
        widgets = {"user_pass": forms.PasswordInput()}
    
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        pass1 = cleaned_data.get('user_pass_check')
        pass2 = cleaned_data.get('user_pass')
        if pass1 != pass2:
            raise forms.ValidationError("The two password fields must match.")
        return cleaned_data
'''


