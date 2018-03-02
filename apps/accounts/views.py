# from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    # ListView,
    # DetailView,
    # CreateView,
    # RedirectView,
)

# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator


# @method_decorator(login_required, name='dispatch')
class UserListView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/users.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UserListView, self).get_context_data(*args, **kwargs)
        context = {
            'page_title': 'Login User List',
        }
        return context
