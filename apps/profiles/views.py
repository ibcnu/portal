from django.views.generic import TemplateView
from apps.profiles.models import UserProfiles, UserSettings

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = "profiles/settings.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        userprofile = UserProfiles()
        # username = userprofile.user.fullname
        # email = userprofile.user.email

        page_title = 'User Profiles'
        context = {
            'page_title': page_title,
            # 'email': email,
            # 'username': username,
        }
        return context


@method_decorator(login_required, name='dispatch')
class SettingsView(TemplateView):
    template_name = "profiles/settings.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SettingsView, self).get_context_data(*args, **kwargs)
        usersettings = UserSettings()
        # username = userprofile.user.fullname
        # email = userprofile.user.email

        page_title = 'User Settings'
        context = {
            'page_title': page_title,
            # 'email': email,
            # 'username': username,
        }
        return context
