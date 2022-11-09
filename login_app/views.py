from xml.dom.domreg import registered
from django.shortcuts import render, HttpResponseRedirect
from login_app.forms import CreateNewUser, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from login_app.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('login_app:login'))
    return render(request, 'login_app/sign_up.html', context={'title': 'Sign Up . DHK', 'form': form})

def login(request):
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password = password)
                if user is None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('App_posts:home'))

        return render(request, 'login_app/login.html', context={'title': 'Log In . DHK', 'form': form})

@login_required

def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)

    return render(request, 'login_app/profile.html', context={'form':form, 'title':'Edit Profile . DHK'})


@login_required

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:login'))