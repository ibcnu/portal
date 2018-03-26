from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Company, Address
from .forms import CompanyCreateForm, AddressCreateForm


class CompanyListView(LoginRequiredMixin, ListView):
    context_object_name = "companies"
    paginate_by = 10

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = None
        if self.request.user.user_profile.role.name != 'Admin' and self.request.user.user_profile.role.name != 'Tech':
            queryset = Company.objects.filter(name=self.request.user.user_profile.company.name)
            # self.request.user.user_profile.assets.all()
        else:
            if slug:
                queryset = Company.objects.fitler(slug=slug)
            else:
                queryset = Company.objects.all()

        # print('CompanyListView:QUERYSET: ', queryset)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Company List'
        context['companies'] = context['object_list']
        # print('CompanyListView:CONTEXT: ', context)
        return context


class CompanyDetailView(LoginRequiredMixin, DetailView):
    queryset = Company.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        company = kwargs.get('object')
        context['page_title'] = 'Company Detail'
        # context['assets'] = Asset.objects.filter(company=company)
        context['assets'] = company.assets.all()
        # context['users'] = DefaultUser.objects.filter(company=company)
        context['users'] = company.users.all()
        # print(company.users.count())
        return context


class CompanyCreateView(LoginRequiredMixin, TemplateView):
    form = CompanyCreateForm
    address_form = AddressCreateForm
    template_name = 'organizations/company_form.html'

    def post(self, request, *args, **kwargs):
        form = CompanyCreateForm(self.request.POST)
        address_form = AddressCreateForm(self.request.POST)

        if form.is_valid() and address_form.is_valid():

            company = form.save(commit=False)
            company.name = form.cleaned_data.get('name') if form.cleaned_data.get('name') else ''
            company.contact = form.cleaned_data.get('contact')
            company.description = form.cleaned_data.get('description') if form.cleaned_data.get('description') else ''
            form.save()

            address = address_form.save(commit=False)
            address.street = self.request.POST.get('street')
            address.street2 = self.request.POST.get('street2')
            address.city = self.request.POST.get('city')
            address.province = self.request.POST.get('province')
            address.postalcode = self.request.POST.get('postalcode')
            address.country = self.request.POST.get('country')

            address.save()
            company.address = address
            form.save()

            c = self.get_context_data()
            return redirect('organizations:company_details', company.slug)
        else:
            # print('forms are invalid')
            c = self.get_context_data()
            c['form'] = form
            c['address_form'] = address_form

        return render(request, self.template_name, c)  # get_context_data()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        form = CompanyCreateForm()
        address_form = AddressCreateForm()
        context['page_title'] = 'Create Company'
        context['form'] = form
        context['address_form'] = address_form
        return context


class CompanyUpdateView(LoginRequiredMixin, TemplateView):
    form = CompanyCreateForm
    address_form = AddressCreateForm

    template_name = 'organizations/company_form.html'
    success_url = reverse_lazy('organizations:company_list')

    def post(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        # print('SLUG: ', slug)
        company = Company.objects.filter(slug=slug).first()
        # print('COMPANY: ', company)

        form = CompanyCreateForm(self.request.POST)
        address_form = AddressCreateForm(self.request.POST)

        if form.is_valid() and address_form.is_valid():
            # print('form and company are valid: ')
            company.name = form.cleaned_data.get('name') if form.cleaned_data.get('name') else ''
            company.contact = form.cleaned_data.get('contact')
            company.description = form.cleaned_data.get('description') if form.cleaned_data.get('description') else ''
            if not company.address:
                company.address = address_form.save()
            company.address.street = self.request.POST.get('street') if self.request.POST.get('street') else ''
            company.address.street2 = self.request.POST.get('street2') if self.request.POST.get('street2') else ''
            company.address.city = self.request.POST.get('city') if self.request.POST.get('city') else ''
            company.address.province = self.request.POST.get('province') if self.request.POST.get('province') else ''
            company.address.postalcode = self.request.POST.get('postalcode') if self.request.POST.get('postalcode') else ''
            company.address.country = self.request.POST.get('country') if self.request.POST.get('country') else ''
            company.address.save()

            # company.company.address = address
            company.save()
            return redirect('organizations:company_details', slug=slug)
        else:
            print('form is not valid: ', form.errors)

        context = self.get_context_data()
        context['form'] = form
        context['address_form'] = address_form

        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        company = Company.objects.filter(slug=self.kwargs.get('slug')).first()

        # print('GETCONTEXT_COMPANY: ', company)
        form = CompanyCreateForm(instance=company)
        address_form = AddressCreateForm(instance=company.address)
        context['page_title'] = 'Update Company'
        context['form'] = form
        context['address_form'] = address_form
        return context


class AddressCreateView(LoginRequiredMixin, CreateView):
    form_class = AddressCreateForm
    template_name = 'organizations/address_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(context)
        context['page_title'] = 'Create Address'
        return context


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AddressCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(context)
        context['page_title'] = 'Update Address'
        return context

    def get_queryset(self):
        return Address.objects.all()


class AddressDetailView(LoginRequiredMixin, DetailView):
    queryset = Address.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(context)
        obj = kwargs.get('object')
        # print(type(obj))
        context['page_title'] = 'Company Detail'
        # context['assets'] = Asset.objects.filter(company=obj)
        # context['users'] = DefaultUser.objects.filter(company=obj)
        return context
