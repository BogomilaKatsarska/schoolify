from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from schoolify.auth_app.forms import SignUpForm, ProfileEditForm
from schoolify.auth_app.models import Profile

UserModel = get_user_model()


def index(request):
    return render(request, 'common/index.html')


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
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


class SignOutView(LoginRequiredMixin, LogoutView):
    template_name = 'auth/sign-out.html'
    next_page = reverse_lazy('index')


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "auth/profile-edit.html"

    def get_success_url(self):
        return reverse('profile details', kwargs={'pk': self.object.pk})

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = "auth/profile-delete.html"
    success_url = reverse_lazy('index')

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk


class ProfileDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    template_name = "auth/profile-details.html"

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk
