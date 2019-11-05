# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from mybay_app.forms import SignUpForm, ProfileForm, LoginForm, ItemForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from mybay_app.models import Profile, Item
from django.contrib import messages

class home_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "main_page.html")
        else:
            login_form = LoginForm()
            return render(request, 'home.html', {"login_form": login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'main_page.html')
            else:
                # meter mensagem de erro aqui
                print("erro")
        else:
            return render(request, 'home.html', {"login_form": login_form})



class signup_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "main_page.html")
        prof_form = ProfileForm()
        signup_form = SignUpForm()
        return render(request, 'signup.html', {"signup_form": signup_form, "prof_form": prof_form})

    def post(self, request):
        signup_form = SignUpForm(request.POST)
        prof_form = ProfileForm(request.POST)
        if signup_form.is_valid():
            signup_form = signup_form.save(commit=False)
            username = signup_form.username
            password = signup_form.password
            signup_form.password = make_password(password)
            signup_form.email = signup_form.username
            signup_form.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                prof_form = prof_form.save(commit=False)
                prof_form.user = request.user
                prof_form.save()
                return render(request, 'main_page.html')
            else:
                # meter mensagem de erro aqui
                print("Erro")
        else:
            return render(request, 'signup.html', {"signup_form": signup_form, "prof_form": prof_form})
    
class item_view(View):
    def get(self, request):
        item_form = ItemForm()
        return render(request, 'item.html', {"item_form": item_form})

    def post(self, request):
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item_form = item_form.save(commit=False)
            item_owner = Profile.objects.get(user=request.user)
            item_form.item_owner = item_owner
            item_form.save()
            item_form = ItemForm()
            messages.success(request, 'Item added')
            return render(request, 'item.html', {'item_form': item_form})
        else:
            # meter erro aqui
            print("Erro")
