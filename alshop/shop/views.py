from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisterUserForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  AuthenticationForm, RegisterUserForm
from django.contrib.auth.views import LoginView
from .models import ForMan, ForWoman

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "shop/login.html"
    
    def get_success_url(self):
        return reverse_lazy('home')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

def home(request):
    return render(request, 'shop/home.html')  # Use 'infiniteway' instead of 'infinteway'


def contact(request):
    return render(request, 'shop/contact.html')

def dashboard(request):
    return render(request, 'shop/dashboard.html')

class ChangeUsername(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ['username']
    template_name = 'shop/change_username.html'
    success_message = "Username updated successfully"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('login')  
    
def products(request):
    return render(request, 'shop/products.html')


def products_view(request):
    men_products = ForMan.objects.all()
    women_products = ForWoman.objects.all()
    return render(request, 'shop/products.html', {
        'men_products': men_products,
        'women_products': women_products,
    })

  
    

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/login")