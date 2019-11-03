from django import forms
from mybay_app.models import AppUser


class SignUpForm(forms.ModelForm):
    user_pass_check = forms.CharField(label="Password confirmation", widget=forms.PasswordInput())
    class Meta:
        model = AppUser
        fields = ["user_email", "user_country", "user_pass"]
        widgets = {"user_pass": forms.PasswordInput()}
    
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        pass1 = cleaned_data.get('user_pass_check')
        pass2 = cleaned_data.get('user_pass')
        if pass1 != pass2:
            raise forms.ValidationError("The two password fields must match.")
        return cleaned_data


