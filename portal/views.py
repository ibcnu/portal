from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
User = get_user_model()


# @login_required(login_url='/account/login/')

# @login_required
@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = "index.html"

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
