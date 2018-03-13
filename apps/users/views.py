from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

# from apps.accounts.models import User
from .models import DefaultUser, UserRole
from .forms import UserForm, ProfileForm, CreateProfileForm


class UserListView(LoginRequiredMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        if self.request.user.user_profile.role.name != 'Admin':
            queryset = DefaultUser.objects.filter(organization=self.request.user.user_profile.organization)
        else:
            queryset = DefaultUser.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'User List'
        print(context)
        return context


class UserDetailView(LoginRequiredMixin, DetailView):
    queryset = DefaultUser.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'User Detail'
        print(context)
        return context


class UserRoleListView(LoginRequiredMixin, ListView):
    template_name = "users/users_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'User List'
        print(context)
        return context


class UserRoleDetailView(LoginRequiredMixin, DetailView):
    queryset = UserRole.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'User Detail'
        print(context)
        return context


class UserUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/defaultuser_form.html'
    success_url = reverse_lazy('users:user_list')

    def post(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        u = DefaultUser.objects.filter(slug=slug).first()

        user_form = UserForm(self.request.POST)
        profile_form = ProfileForm(self.request.POST)

        if profile_form.is_valid() and u:
            print('form is valid and u')
            print(u)

            u.bio = profile_form.cleaned_data.get('bio') if profile_form.cleaned_data.get('bio') else ''
            u.phone = profile_form.cleaned_data.get('phone') if profile_form.cleaned_data.get('phone') else ''
            u.city = profile_form.cleaned_data.get('city') if profile_form.cleaned_data.get('city') else ''
            u.country = profile_form.cleaned_data.get('country') if profile_form.cleaned_data.get('country') else ''
            u.role = profile_form.cleaned_data.get('role')
            u.organization = profile_form.cleaned_data.get('organization')
            u.save()

            print(u.role)
            account = u.user
            account.fullname = self.request.POST.get('fullname')
            if self.request.POST.get('active') == 'on':
                account.active = True
            else:
                account.active = False

            print(self.request.POST.get('active'))
            print(account.active)
            account.save()
            # profile_form.save()
            return redirect('users:user_detail', slug=slug)
        else:
            print('profile_form is not valid')
            print(profile_form.errors)

        context = self.get_context_data()
        context['user_form'] = user_form
        context['profile_form'] = profile_form

        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        u = DefaultUser.objects.filter(slug=self.kwargs.get('slug')).first()
        user_form = UserForm(instance=u.user)
        profile_form = ProfileForm(instance=u)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'page_title': 'Edit User',
            'defaultuser': u,
        }
        return context


class UserCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/defaultuser_form.html'
    msg = ''

    def post(self, request, *args, **kwargs):
        user_form = UserForm(self.request.POST)
        profile_form = CreateProfileForm(self.request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print('form are valid')
            password1 = user_form.cleaned_data.get('password1')
            password2 = user_form.cleaned_data.get('password2')
            fullname = user_form.cleaned_data.get('fullname')
            email = user_form.cleaned_data.get('email')

            user = user_form.save(commit=False)
            self.create_user(user, fullname, email, password1, password2)

            print('profile_form is valid')
            print('saving user')
            user.save()
            print('user saved')
            print(user)

            newuser = user.user_profile
            print(type(newuser))
            # newuser.bio = profile_form.cleaned_data.get('bio')
            newuser.phone = profile_form.cleaned_data.get('phone')
            newuser.city = profile_form.cleaned_data.get('city')
            newuser.country = profile_form.cleaned_data.get('country')
            newuser.role = profile_form.cleaned_data.get('role')
            newuser.organization = profile_form.cleaned_data.get('organization')
            newuser.save()

            c = self.get_context_data()
            return redirect('users:user_detail', newuser.slug)
        else:
            print('forms are invalid')
            c = self.get_context_data()
            c['user_form'] = user_form
            c['profile_form'] = profile_form

        return render(request, self.template_name, c)  # get_context_data()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user_form = UserForm()
        profile_form = CreateProfileForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'page_title': 'Create User',
            'err_msg': self.msg,
        }
        return context

    def create_user(self, user, fullname, email, password1, password2):
        if password1 != password2:
            self.msg = 'Passwords fo not match'
            # messages.error(self.request, self.msg, extra_tags='alert alert-danger')
            # self.context['messages'] = messages
            return render(self.request, self.template_name, self.context)
        user.fullname = fullname
        user.email = email
        user.set_password(password1)
