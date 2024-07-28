from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from users.forms import UserCreateForm, UserUpdateForm


# Create your views here.

class RegisterView(CreateView):
    def get(self, request, *args, **kwargs):
        create_form = UserCreateForm()
        context = {'form': create_form}
        return render(request, 'users/register.html', context)

    def post(self, request, *args, **kwargs):
        # create user account

        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            create_form = UserCreateForm()
            context = {'form': create_form}
            return render(request, 'users/register.html', context)


class LoginView(FormView):
    def get(self, request, *args, **kwargs):
        login_form = AuthenticationForm()

        return render(request, 'users/login.html', {'login_form': login_form})

    def post(self, request, *args, **kwargs):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())
            messages.success(request, 'You are now logged in.')

            return redirect('books:list')
        else:
            return render(request, 'users/login.html', {'login_form': login_form})

    def test_logout(self):
        db_user = CustomUser.objects.create_user(username='test', first_name='test', last_name='test')
        db_user.set_password('memome')
        db_user.save()



class ProfileView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/profile.html', {"user": request.user})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    def get(self, request, *args, **kwargs):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, 'users/profile_edit.html', {"form": user_update_form})

    def post(self, request, *args, **kwargs):
        user_update_form = UserUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('users:profile')
        else:
            return render(request, 'users/profile_edit.html', {"form": user_update_form})
class LogoutView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request,'You have been logged out.')
        return redirect('landing_page')