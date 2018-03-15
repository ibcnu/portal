# from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Asset, AssetType
from apps.issues.models import Issue
from .forms import AssetCreateForm


class AssetListView(LoginRequiredMixin, ListView):
    paginate_by = 5
    context_object_name = "assets"
    atype = ''

    def get_queryset(self, *args, **kwargs):
        queryset = Asset.objects.all()
        if self.request.user.user_profile.role.name != 'Admin':
            queryset = self.request.user.user_profile.assets.all()

        self.atype = self.kwargs.get('atype')
        if self.atype:
            queryset = queryset.filter(assettype__in=AssetType.objects.filter(name=self.atype))
        print()

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(AssetListView, self).get_context_data(*args, **kwargs)
        context['page_title'] = 'Product List'
        context['atype'] = self.atype
        # print(context)
        return context


class AssetDetailView(LoginRequiredMixin, DetailView):
    queryset = Asset.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # if self.request.user.user_profile.role.name != 'Admin':
        asset = kwargs.get('object')
        context['page_title'] = 'Product Detail'
        context['issues'] = asset.issues.all()
        context['users'] = asset.users.all()
        print(asset.users)
        return context


class AssetCreateView(LoginRequiredMixin, CreateView):
    form_class = AssetCreateForm
    template_name = 'assets/asset_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print('AssetCreateView:GET', self.request.GET['cid'])
        print('AssetCreateView:kwargs', kwargs)
        context['page_title'] = 'Create Product'
        context['cid'] = self.request.GET['cid']
        print('AssetCreateView:Context', context)
        return context


class AssetUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AssetCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Update Product'
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
