from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.shortcuts import render


def sign_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/polls')
    else:
        return render(request, 'account/signin.html')


def sign_up(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/polls')
    else:
        return render(request, 'account/signup.html')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            return render(request, 'account/signin.html', {'error_message': _("ACCOUNT_DISABLED")})
    else:
        return render(request, 'account/signin.html', {'error_message': _("LOGIN_INVALID_DATA")})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:signin'))


def register(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['repeat_password']

    try:
        user = User.objects.get(email=email)
        return render(request, 'account/signup.html', {'error_message': _("USER_ALREADY_EXISTS")})
    except:
        if password == password2:
            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()

            return render(request, 'account/signin.html', {'error_message': _("REGISTERED_SUCCESSFULLY")})
        else:
            return render(request, 'account/signup.html', {'error_message': _("PASSWORD_DO_NOT_MATCH")})
