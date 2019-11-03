# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from mybay_app.forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password

class home_view(View):
    def get(self, request):
        return render(request, 'test.html')


class signup_view(View):
    def get(self, request):
        signup_form = SignUpForm()
        return render(request, 'signup.html', {"forms": signup_form})
    def post(self, request):
        signup_form = SignUpForm(data=request.POST)
        if signup_form.is_valid():
            email = signup_form.cleaned_data.get('user_email')
            password = signup_form.cleaned_data.get('user_pass')
            print("Original password is: ", password)
            hashed_password = make_password(password)
            print("Hashed password is: ", hashed_password)
            signup_form.inital['user_pass'] = hashed_password 
            signup_form.save()
            request.session['username'] = email
            return render(request, 'main_page.html')
        else:
            return render(request, 'signup.html', {"forms": signup_form})

# Create your views here.
