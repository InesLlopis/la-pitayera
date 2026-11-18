# UD 5.2
from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
class LoginFormView(LoginView):
    template_name = 'login/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context