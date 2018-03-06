from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from .models import Company
from .forms import CompanyCreateForm


class CompanyListView(LoginRequiredMixin, ListView):
    # template_name = "organizations/company_list.html"
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Company.objects.fitler(
                Q(name__iexact=slug) |
                Q(name__contains=slug)
            )
        else:
            queryset = Company.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Company List'
        return context


class CompanyDetailView(LoginRequiredMixin, DetailView):
    queryset = Company.objects.all()
    # template_name = "organizations/company_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Company Detail'
        return context


class CompanyCreateView(LoginRequiredMixin, CreateView):
    # model = Company
    form_class = CompanyCreateForm
    template_name = 'organizations/company_form.html'
    # success_url = 'organizations/company_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Create Company'
        return context


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    # model = Company
    # fields = ("name", "contact", 'address', 'description')
    form_class = CompanyCreateForm
    # template_name = 'organizations/company_form.html'
    # success_url = reverse_lazy('organizations:company_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Update Company'
        return context

    def get_queryset(self):
        return Company.objects.all()
