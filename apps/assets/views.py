# from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Asset
from .forms import AssetCreateForm


class AssetListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        # slug = self.kwargs.get('slug')
        queryset = Asset.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(AssetListView, self).get_context_data(*args, **kwargs)
        context['page_title'] = 'Asset List'
        return context


class AssetDetailView(LoginRequiredMixin, DetailView):
    queryset = Asset.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Asset Detail'
        print(context)
        return context


class AssetCreateView(LoginRequiredMixin, CreateView):
    form_class = AssetCreateForm
    template_name = 'assets/asset_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Create Asset'
        return context


class AssetUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AssetCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Update Asset'
        return context

    def get_queryset(self):
        return Asset.objects.all()


# class AssetTypeCreateView(LoginRequiredMixin, View):
#     model = AssetType
#     template_name = 'assets/asset_form.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         print(context)
#         context['page_title'] = 'Create Asset'
#         return context
