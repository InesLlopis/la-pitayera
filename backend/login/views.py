# UD 5.2
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

# Create your views here.
class LoginFormView(LoginView):
    template_name = 'login/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('panel')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context