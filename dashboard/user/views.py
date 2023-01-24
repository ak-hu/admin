
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpRequest

import base64
import pickle


from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginUserForm, AddUserForm, UpdateUserForm
from .models import Main


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'
    extra_context = {'title': 'Login'}


@login_required(login_url='login')
def profile(request):
    users = Main.objects.all()
    header = f"<h1 class='mb-4'>All users</h1>"

    context = {
        'users': users,
        'title': 'User Manager Dashboard',
        'header': header
    }

    return (request, 'user/profile.html', context)


@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AddUserForm()
    context = {
        'form': form,
        'title': 'Add New User'
    }
    return render(request, 'user/add_user.html', context)


@login_required(login_url='login')
def edit(request, pk):
    id = Main.find(_id)
    pk = user._id
    user = Main.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=user)
    
    context = {
        'title': 'Update User',
        'form': form, 
    }
    return render(request, 'user/edit_profile.html', context)


@login_required(login_url='login')
@csrf_exempt
def delete(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        Main.objects.get(id=user_id).delete()

        return JsonResponse({'bool': True})