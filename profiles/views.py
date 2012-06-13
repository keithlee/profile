# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError, Http404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth.models import User 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,sessions
from forms import UserProfileForm 
from django.contrib.auth.models import User
from profiles.models import *
# username and email are the same

def index(request):
    return render_to_response('registration/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        if password1 != password2:
            messages.add_message(request, messages.INFO,"The passwords do not match")
            return render(request, 'registration/register.html')
        # Password hashing problem in Django 1.4
#        user, created =  User.objects.get_or_create(username=username, defaults={'password': password1})
        if User.objects.filter(username=username).count() > 0:
            messages.add_message(request, messages.ERROR,"A profile has already been created with that email address")
            return render(request, 'registration/register.html')
        else:
            User.objects.create_user(username, username, password1)
            return HttpResponseRedirect('/account/')
    return render_to_response('registration/register.html', context_instance=RequestContext(request))

def account(request): 
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    user = User.objects.get(pk=request.user.id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        slug = request.POST['slug']
        if User.objects.filter(userprofile__slug=slug).count()> 0:
            messages.add_message(request, messages.ERROR,"The slug",slug,"has been taken")
            return render(request, 'profiles/account.html')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+request.POST['slug'])
        else:
            return render(request, 'profiles/account.html')
    else:
#        form = UserProfileForm(request.POST, request.FILES, instance = user.profile)
        form = UserProfileForm(request.POST, request.FILES, instance = user.profile)
#        return render_to_response('profiles/home.html', { 'form' : form}, context_instance=RequestContext(request))
    return render_to_response('profiles/account.html', { 'form' : form}, context_instance=RequestContext(request))

def profile(request, slug):
    user = User.objects.get(userprofile__slug=slug)
#    user = User.objects.get(pk=request.user.id)
    return render_to_response('profiles/profilePage.html', {'user': user})
    

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")



