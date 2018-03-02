from django.views.generic import TemplateView


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class CompanyListView(TemplateView):
    template_name = "organizations/company_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyListView, self).get_context_data(*args, **kwargs)
        context = {
            'page_title': 'Company List',
        }
        return context
