# from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AssetCreateForm
from .models import Asset, AssetType
from apps.issues.models import Issue


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

        return queryset

    def get_page_title(self, type_name, *args, **kwargs):
        pgtitle = 'Product'
        # page_title = 'Product List'
        print(type_name)
        if type_name:
            assettype = AssetType.objects.get(name=type_name)
            pgtitle = assettype.value
        pgtitle = pgtitle + ' List'
        print(pgtitle)
        return pgtitle

    def get_context_data(self, *args, **kwargs):
        context = super(AssetListView, self).get_context_data(*args, **kwargs)
        print(self.get_page_title(self.atype))
        context['page_title'] = self.get_page_title(self.atype)
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
        context['pid'] = asset.id
        # print(asset.users)
        return context


class AssetCreateView(LoginRequiredMixin, CreateView):
    form_class = AssetCreateForm
    template_name = 'assets/asset_form.html'

    def form_valid(self, form):
        print('AssetCreateView:form_valid()')
        return super(AssetCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print('AssetCreateView:GET', self.request.GET['cid'])
        # print('AssetCreateView:kwargs', kwargs)
        context['page_title'] = 'Create Product'
        context['cid'] = self.request.GET['cid']
        context['atype'] = self.request.GET['atype']
        # print('AssetCreateView:Context', context)
        return context


class AssetUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AssetCreateForm

    def form_valid(self, form):
        print('AssetUpdateView:form_valid()')
        return super(AssetUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(context)
        context['page_title'] = 'Update Product'
        return context

    def get_queryset(self):
        return Asset.objects.all()
