# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from mybay_app.forms import SignUpForm, ProfileForm, LoginForm, ItemForm, UserDeleteForm, UserEditForm, SearchForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from mybay_app.models import Profile, Item
from django.contrib import messages

class home_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('mainpage')
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
                return redirect('mainpage')
            else:
                # meter mensagem de erro aqui
                print("erro")
        else:
            return render(request, 'home.html', {"login_form": login_form})



class signup_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('mainpage')
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
                return redirect('mainpage')
            else:
                # meter mensagem de erro aqui
                print("Erro")
        else:
            return render(request, 'signup.html', {"signup_form": signup_form, "prof_form": prof_form})
    
class item_view(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
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

def logout_view(request):
    logout(request)
    login_form = LoginForm()
    return redirect('home')


class user_delete_view(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        user_delete_form = UserDeleteForm()
        return render(request, 'user_delete.html', {'user_delete_form': user_delete_form})

    def post(self, request):
        user_delete_form = UserDeleteForm(request.POST)
        user = request.user
        if user_delete_form.data['password'] == user_delete_form.data['password_check'] and user.check_password(user_delete_form.data['password']):
            user_profile = Profile.objects.get(user=user)
            user.delete()
            user_profile.delete()
            return redirect('home')
        else:
            #meter erro aqui
            return render(request, 'user_delete.html', {'user_delete_form': user_delete_form})

class user_edit_view(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        user_edit_form = UserEditForm()
        return render(request, 'user_edit.html', {'user_edit_form': user_edit_form})

    def post(self, request):
        user_edit_form = UserEditForm(request.POST)
        user = request.user
        user_profile = Profile.objects.get(user=user) 
        if user_edit_form.is_valid() and user.check_password(user_edit_form.data['old_password']):
            user.password = make_password(user_edit_form.data['new_password'])
            user.username = user_edit_form.data['new_username']
            user.email = user_edit_form.data['new_username']
            user_profile.user_country = user_edit_form.data['new_country']
            user.save()
            user_profile.save()
            return render(request, 'home.html')
        else:
            #meter erro aqui
            print('erro')
            return render(request, 'user_edit.html', {'user_edit_form': user_edit_form})

class item_edit_view(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        return render(request, 'item_edit.html')

    def post(self, request):
        user = request.user
        user_profile = Profile.objects.get(user=user) 
        list_of_items = Item.objects.filter(item_owner=user_profile)
        print(list_of_items)
        return render(request, 'item_edit.html')

class home_page_view(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        item_list = Item.objects.all()
        search_form = SearchForm()
        return render(request, 'main_page.html', {'item_list': item_list, 'search_form': search_form})
    
    def post(self, request):
        if 'search_text' in request.POST:
            search_text = request.POST['search_text']
            item_list = Item.objects.filter(item_name__contains=search_text)
            search_form = SearchForm()
            return render(request, 'main_page.html', {'item_list': item_list, 'search_form': search_form})
        else:
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                cat_sel = search_form.cleaned_data.get('category_select')
                my_country = search_form.cleaned_data.get('my_country')
                name_select = search_form.cleaned_data.get('name_select')
                price_min = search_form.cleaned_data.get('price_min')
                price_max = search_form.cleaned_data.get('price_max')
                date_select = search_form.cleaned_data.get('date_select')
                after_date = search_form.cleaned_data.get('after_date')
                print("form info")
                print("my_country: ", my_country)
                print("name_select: ", name_select)
                print("price_min: ", price_min)
                print("price_max: ", price_max)
                print("date_select: ", date_select)
                print("after_date: ", after_date)

                #fetch all objects
                item_list = Item.objects.all()

                #if category is selected, filter by it
                if cat_sel is not '':
                    item_list = Item.objects.filter(item_category=cat_sel)
                
                #fazer para country
                
                #if ascending or descending is selected by name, filter by it
                if name_select is not '':
                    if name_select == 'ascending':
                        item_list = item_list.order_by('item_name')
                    else:
                        item_list = item_list.order_by('-item_name')
                
                #if there is a min price
                if price_min is not None:
                    item_list = item_list.filter(item_price__gte=price_min)
                
                #if there is a max price
                if price_max is not None:
                    item_list = item_list.filter(item_price__lte=price_max)
                
                if date_select is not '':
                    if date_select == 'ascending':
                        item_list = item_list.order_by('item_date')
                    else:
                        item_list = item_list.order_by('-item_date')
                
                if after_date is not None:
                    item_list = item_list.order_by(item_date__gt=after_date)
                
                search_form = SearchForm()
                print(item_list)
                return render(request, 'main_page.html', {'item_list': item_list, 'search_form': search_form})
            else:
                print("ripppp")
        return redirect('home')

class profile_view(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        my_user = request.user
        my_profile = Profile.objects.get(user=my_user)
        item_list = Item.objects.filter(item_owner=my_profile).order_by('item_date')
        return render(request, 'profile.html', {'item_list': item_list})
    def post(self, request):
        return render(request, 'profile.html')

    
 
