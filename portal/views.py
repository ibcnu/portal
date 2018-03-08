
from apps.assets.forms import AssetTypeCreateForm
from apps.assets.models import AssetType
from apps.issues.models import IssueStatus, IssueType
from apps.users.forms import UserRoleCreateForm
from apps.users.models import UserRole

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings
User = settings.AUTH_USER_MODEL


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
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
