from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *

menu = [
    {'title': 'Главная','url': '/'},
    {'title': 'О нас','url': '/'},
    {'title': 'Ещё что то','url': '/'}
]


# Create your views here.
def index_page(request):
    return render(request, 'main/index.html', context={'menu': menu})


class RegisterUser(CreateView):  # страница регистрации (написанная через классы представления)
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):  # делаем наполнение
        context = {
            'menu': menu,
            'form': self.get_form(),
        }
        return context

    def form_valid(self, form):  # логиним если всё нормально
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):  # страница логина (написанная через классы представления)
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):  # делаем наполнение
        context = {
            'menu': menu,
            'form': self.get_form(),
        }
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logoutUser(request):  # функция выхода
    logout(request)
    return redirect('home')
