
from apps.assets.forms import AssetTypeCreateForm
from apps.assets.models import AssetType
from apps.issues.models import IssueStatus, IssueType
from apps.users.forms import UserRoleCreateForm
from apps.users.models import UserRole

from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings

from apps.organizations.models import Company
from apps.assets.models import Asset
from apps.users.models import DefaultUser

User = settings.AUTH_USER_MODEL


class CompanyIndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user.user_profile
        company = user.company
        context['company'] = company
        context['page_title'] = 'Company Detail'
        context['assets'] = Asset.objects.filter(company=company)
        context['users'] = DefaultUser.objects.filter(company=company)
        print(context)
        return context


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.request.user.user_profile.role)
        print(dir(self.request.user.user_profile))
        context = {
            'page_title': 'Dashboard',
        }
        return context


class SiteSettingsView(LoginRequiredMixin, TemplateView):
    template_name = "settings.html"
    assettypeform = AssetTypeCreateForm()
    userroleform = UserRoleCreateForm()

    # def get(self, request, *args, **kwargs):
    #     pass
    # def post(self, request, *args, **kwargs):
    # assettypeform = AssetTypeCreateForm(request.POST)
    # userroleform = UserRoleCreateForm(request.POST)
    # if all(assettypeform.is_valid(), userroleform.is_valid()):
    #     pass

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Site Settings'
        context['assettypes'] = AssetType.objects.all()
        context['assettype_form'] = self.assettypeform
        context['issuetypes'] = IssueType.objects.all()
        context['statuses'] = IssueStatus.objects.all()
        context['userroles'] = UserRole.objects.all()
        context['role_form'] = self.userroleform
        print(context)
        return context
