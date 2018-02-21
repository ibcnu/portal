from django.conf import settings
from django.views.generic import TemplateView
from apps.profiles.models import UserProfiles


class ProfileView(TemplateView):
    template_name = settings.CURRENT_TEMPLATE + "/settings.html"

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
