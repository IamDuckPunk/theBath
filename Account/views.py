from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponse, HttpResponseRedirect
from Account.models import UserProfile
from django.contrib.auth.models import User
from Account.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    print(userprofile.favourite_albums.all())
    args = {
        'user': user,
        'userprofile': userprofile
    }
    return render(request, 'accounts/profile.html', args)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'user_picture' in request.FILES:
                profile.user_picture = request.FILES['user_picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'accounts/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                   })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'accounts/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
