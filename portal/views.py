from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
User = get_user_model()


class IndexView(TemplateView):
    template_name = settings.CURRENT_TEMPLATE + "/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        user = User()
        username = user.fullname
        username = user.email
        username = 'Barry Huffman'

        page_title = 'Dashboard'
        context = {
            'page_title': page_title,
            'username': username
        }
        return context
