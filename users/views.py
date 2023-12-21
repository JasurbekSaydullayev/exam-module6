from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .forms import LoginUsersForm, RegisterUsersForm


# Create your views here.


class LoginUser(LoginView):
    form_class = LoginUsersForm
    template_name = 'registration/login.html'
    extra_context = {'title': 'Kirish'}

    def get_success_url(self):
        return reverse_lazy('quiz')


def login_user(request):
    if request.method.upper() == 'POST':
        form = LoginUsersForm(request.POST)
        # print(form)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password1'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('quiz'))
    else:
        form = LoginUsersForm()
    return render(request, 'login', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def register(request):
    if request.method == 'POST':
        form = RegisterUsersForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'registration/register_done.html')
    else:
        form = RegisterUsersForm
    return render(request, 'registration/register.html', {'form': form})
