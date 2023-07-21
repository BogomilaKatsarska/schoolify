from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from schoolify.auth_app.forms import SignUpForm


def index(request):
    return render(request, 'common/base.html')


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    #form_class is the form that is used to create our users
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(LogoutView):
    template_name = 'auth/sign-out.html'
    next_page = reverse_lazy('index')

#TODO: password change view