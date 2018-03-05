from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from .models import DefaultUser, UserRole
from .forms import UserCreateForm, UserForm


class UserListView(LoginRequiredMixin, ListView):
    # template_name = "users/users_list.html"
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = DefaultUser.objects.fitler(
                Q(fullname__iexact=slug) |
                Q(name__contains=slug)
            )
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


class UserCreateView(LoginRequiredMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'users/defaultuser-update.html'
    # success_url = reverse_lazy('users/user_list.html')

    def form_valid(self, form):
        print("called form_valid")
        context = {'form', form, }

        user = form.save(commit=False)
        fullname = form.cleaned_data.get('fullname')
        email = form.cleaned_data.get('email')
        bio = form.cleaned_data.get('bio')
        phone = form.cleaned_data.get('phone')
        city = form.cleaned_data.get('city')
        country = form.cleaned_data.get('country')
        role = form.cleaned_data.get('role')
        organization = form.cleaned_data.get('organization')
        slug = form.cleaned_data.get('slug')

        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')
        if password != password2:
            print('password are good')
            messages.error(self.request, "Passwords fo not match", extra_tags='alert alert-danger')
            return render(self.request, self.template_name, context)
        user.fullname = fullname
        user.email = email
        user.set_password(password)
        print('saving user')
        user.save()
        print('user saved')

        print('creating profile')
        DefaultUser.objects.create(
            user=user,
            bio=bio,
            phone=phone,
            city=city,
            country=country,
            role=role,
            organization=organization,
        )
        print('profile created')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'User Create'
        print(context)
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    template_name = 'users/defaultuser-update.html'
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'User Update'
        # context['user'] = self.request.user
        # context['form2'] = self.form_class2
        print(context)
        return context

    def get_queryset(self):
        return DefaultUser.objects.filter(user=self.request.user)


# def UserNProfileUpdateView(request, slug):

#     if request.method == 'POST':
#         user_form = UserForm(request.POST, prefix='usr')
#         profile_form = UserCreateForm(request.POST, prefix='prof')

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             profile = profile_form.save()
#             return redirect(user)

#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = UserCreateForm(instance=request.user.profile)

#     return render(request, 'users/defaultuser-update.html', {
#         'user_form': user_form,
#         'profile_form': profile_form,
#     })


# class UserNProfileUpdateView2(LoginRequiredMixin, UpdateView):
#     form_class = UserCreateForm
#     second_form_class = UserForm
#     template_name = 'users/defaultuser-update.html'
#     success_url = 'users/user_list.html'


#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['page_title'] = 'Update User'
#         print(context)
#         return context

#     def get_queryset(self):
#         return DefaultUser.objects.filter(user=self.request.user)


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
