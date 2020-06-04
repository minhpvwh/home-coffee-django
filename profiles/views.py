from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, FormView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
# from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from captcha.fields import ReCaptchaField
from profiles.forms import RegisterForm
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class SiteLoginView(LoginView):
    template_name = 'login.html'


class SiteRegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(username=data["username"], password=data["password1"],
                                            email=data["email"])
        from pprint import pprint;
        pprint(data)
        url = f"{reverse('register_ok')}?username={new_user.username}"
        print(url)
        from pprint import pprint;
        pprint(url)
        return redirect(url)


class SiteRegisterOkView(TemplateView):
    template_name = 'register_ok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context


class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class SiteLogoutView(LogoutView):
    template_name = 'logout.html'

class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    model = User
    fields = ("full_name", "address", "year_birth", "about")
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
