# from django.conf import settings
# User = settings.AUTH_USER_MODEL

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
# from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView  # , View

from .forms import AssetCreateForm, AssetUserUpdateForm
from .models import Asset, AssetType  # , AssetUser

from apps.accounts.models import User
# from apps.issues.models import Issue
from apps.users.models import DefaultUser


class AssetListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    context_object_name = "assets"
    atype = ''

    def get_queryset(self, *args, **kwargs):
        queryset = Asset.objects.all()
        print()
        print('AssetListView:get_queryset: ', queryset)
        if self.request.user.user_profile.role.name != 'Admin' and self.request.user.user_profile.role.name != 'Tech':
            queryset = self.request.user.user_profile.assets.all()

        self.atype = self.kwargs.get('atype')
        if self.atype:
            queryset = queryset.filter(assettype__in=AssetType.objects.filter(name=self.atype))

        print()
        print('AssetListView:get_queryset: ', queryset)
        return queryset

    def get_page_title(self, type_name, *args, **kwargs):
        pgtitle = 'Product'
        if type_name:
            assettype = AssetType.objects.get(name=type_name)
            pgtitle = assettype.value
        pgtitle = pgtitle + ' List'
        return pgtitle

    def get_context_data(self, *args, **kwargs):
        context = super(AssetListView, self).get_context_data(*args, **kwargs)
        context['Product_page_title'] = self.get_page_title(self.atype)
        context['atype'] = self.atype

        paginator = Paginator(contact_list, paginate_by)

        print(context)
        return context


class AssetDetailView(LoginRequiredMixin, DetailView):
    queryset = Asset.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # if self.request.user.user_profile.role.name != 'Admin' and self.request.user.user_profile.role.name != 'Tech':
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

    # def post(self, request, *args, **kwargs):
    #     form = AssetCreateForm(self.request.POST)
    #     if not form.is_valid():
    #         print('==========================================')
    #         print('AssetUpdateView:FORM_ERRORS: ', form.errors)
    #     return super(AssetUpdateView, self).post(request, *args, **kwargs)

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


class AssetUsersView(LoginRequiredMixin, TemplateView):
    template_name = 'assets/asset_users.html'
    form = AssetUserUpdateForm

    # def form_valid(self, form):
    #     print('AssetUsersView:form_valid()')
    #     return super(AssetUsersView, self).form_valid(form)

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     # print(context)
    #     context['page_title'] = 'Update Product Users'
    #     return context

    def post(self, request, *args, **kwargs):
        form = AssetUserUpdateForm(self.request.POST)

        if form.is_valid():
            print('Form is valid')
        else:
            # print('forms are invalid')
            c = self.get_context_data()
            c['form'] = form
            # c['address_form'] = address_form

        return render(request, self.template_name, c)  # get_context_data()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print('ARGS: ', args)
        print('KWARGS: ', kwargs)
        print('REQUEST.GET: ', self.request.GET.get('s'))
        asset = Asset.objects.filter(slug=self.request.GET.get('s'))
        form = AssetUserUpdateForm(asset=asset.first())
        context['page_title'] = 'User List'
        context['form'] = form
        context['asset'] = asset.first()
        # context['address_form'] = address_form
        print(context)
        return context

    def get_queryset(self):
        return User.objects.all()

    # def get_queryset(self, *args, **kwargs):
    #     print('AssetUserUpdateView:GET_QS:WKARGS: ', kwargs)
    #     return User.objects.all()


def asset_users_change_view(request, operation, pk, asset_pk):
    print('PK: ', pk, ' | assetPK: ', asset_pk, ' | operation: ', operation, '| Path: ', request.GET.get('next'))
    user = DefaultUser.objects.get(pk=pk)
    asset = Asset.objects.get(pk=asset_pk)
    if operation == 'add':
        asset.add_user_to_asset(user)
    elif operation == 'remove':
        asset.remove_user_from_asset(user)

    print(user)
    print(asset.slug)
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    # return reverse('assets:asset_details', kwargs={'slug': asset.slug})
    # return render('index')
    # return render('assets:asset_details', {'slug': asset.slug})
    return redirect('assets:asset_details', asset.slug)
    # return redirect(path)


# class AssetUserUpdateView(LoginRequiredMixin, UpdateView):
#     pass
#     form_class = AssetUserUpdateForm

#     def get_queryset(self, *args, **kwargs):
#         print('AssetUserUpdateView:GET_QS:WKARGS: ', kwargs)
#         return AssetUser.objects.all()
