from __future__ import unicode_literals
from . models import *
from django.shortcuts import render, redirect #HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'all_users': User.objects.all(),
        'all_friends': Friend.objects.all(),
    }
    return render(request, 'friends/index.html', context)

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    # print(Friend.objects.all())
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        # 'my_friends': Friend.objects.all(),
        'non_friends': User.objects.all(),
    }
    return render(request, 'friends/success.html', context)

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def add(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/{{user_id}}')
    user = User.objects.get(id=request.session['user_id'])
    Friend.objects.create(id=request.POST['friend_id'], user = user)
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return redirect('friends/success.html')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'friends/show.html', context)


def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/friends')