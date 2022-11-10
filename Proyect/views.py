from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from Proyect.models import Empleado
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User

def about(request):
    return render(request, "Proyect/about.html")

class ListEmpleado(LoginRequiredMixin, ListView):
    model = Empleado

class CreateEmpleado(SuccessMessageMixin ,CreateView):
    model = Empleado
    form = Empleado
    success_url = reverse_lazy("list-empleado")
    fields = ["name", "last_name", "age", "area", "legajo", "contacto", "email", "date", "avatar"]
    
class DeleteEmpleado(DeleteView):
    model = Empleado
    success_url = reverse_lazy("list-empleado")

class ActualizarEmpleado(UpdateView):
    model = Empleado
    success_url = reverse_lazy("list-empleado")
    fields = ["name", "last_name", "age", "area", "legajo", "contacto", "email", "date", "avatar"]

class DetailEmpleado(DetailView):
    model = Empleado
    
class LoginEmpleado(LoginView):
    template_name = "Proyect/empleado_login.html"
    success_url = "/inicio"
    # nex_page = reverse_lazy("list-empleado")

class LogoutEmpleado(LogoutView):
    template_name = "Proyect/empleado_logout.html"
    
class SignUpEmpleado(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login-empleado")
    template_name = "registration/signup.html"

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("login-empleado")