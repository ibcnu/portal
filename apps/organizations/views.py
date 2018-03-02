# from django.views.generic import TemplateView
from django.views.generic import TemplateView, DetailView, ListView

from .models import Company

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class CompanyListView(TemplateView):
    template_name = "organizations/company_list.html"
    # models = Company

    # def get_template_names(self):
    #     return "organizations/company_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context = {
            'page_title': 'Company List',
        }
        return context


# @method_decorator(login_required, name='dispatch')
# class CompanyDetailView(TemplateView):
#     template_name = "organizations/company_detail.html"
#     model = Company

#     def get_template_names(self):
#         return "organizations/company_detail.html"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context = {
#             'page_title': 'Company Detail',
#         }
#         return context
