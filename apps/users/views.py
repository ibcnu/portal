# from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class UserListView(TemplateView):
    template_name = "users/users_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UserListView, self).get_context_data(*args, **kwargs)
        context = {
            'page_title': 'User List',
        }
        return context
