### common includes
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy



from django.conf import settings
User = settings.AUTH_USER_MODEL

<input type="hidden" name="next" value="{{ request.path }}">
next = request.POST.get('next', '/')
return HttpResponseRedirect(next)
<a href="{% url 'your_form_view' %}?next={{ request.path|urlencode }}">Go to my form!</a>
{{ request.GET.next }}

, related_name='company'
### VIEWS
class [model]ListView(LoginRequiredMixin, ListView):
    [template_name = "[app]/[model]_list.html"]
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = [model].objects.fitler(
                Q([feild]__iexact=slug) |
                Q([feild]__contains=slug)
            )
        else:
            queryset = [model].objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = '[model] List'
        print(context)
        return context


class [model]DetailView(LoginRequiredMixin, DetailView):
    queryset = [model].objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = '[model] Detail'
        print(context)
        return context


class [model]CreateView(LoginRequiredMixin, CreateView):
    [[model = [model] | form_class = [model]CreateForm]]
    template_name = '[app]/[model]_form.html'
    [success_url = '[app]/[model]_list.html']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Create [model]'
        return context


class [model]UpdateView(LoginRequiredMixin, UpdateView):
    [[model = [model] |
    form_class = [model]CreateForm
    fields = ("name", "contact", 'address', 'description')]]

    [template_name = '[app]/[model]_form.html']
    [success_url = reverse_lazy('[app]:[model]_list')]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Update [model]'
        return context

    def get_queryset(self):
        return [model].objects.all()



        kw_args = {}
        if self.request.user.user_profile.role != 'Admin':
            kw_args['organization'] = self.request.user.user_profile.organization
        slug = self.kwargs.get('slug')
        if slug:
            kw_args['fullname__iexact'] = slug

        if kw_args:
            queryset = DefaultUser.objects.filter(**kw_args)
        else:
            queryset = DefaultUser.objects.all()
        return queryset


### MODEL FIELDS
models.CharField(max_length=255, null=False, blank=False, default=None)
models.ForeignKey([model], models.[SET_NULL], blank=True, null=True,)

timestamp = models.DateTimeField(auto_now_add=True)
updated = models.DateTimeField(auto_now=True)
slug = models.SlugField(max_length=50)


### URLS
from django.urls import path
from .views import [model]ListView, [model]DetailView, [model]CreateView, [model]UpdateView

app_name = '[app]'
urlpatterns = [
    path('', [model]ListView.as_view(), name='[model]_list'),
    path('create/', [model]CreateView.as_view(), name='[model]_create'),
    path('edit/<slug:slug>/', [model]UpdateView.as_view(), name='[model]_edit'),
    path('<slug:slug>/', [model]DetailView.as_view(), name='[model]_details'),
]



### FORMS
class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [ ]


### ADMIN
from django.contrib import admin
from .models import [model]
admin.site.register([model])


### TEMPLATES
{% extends "base.html" %}
{% load static widget_tweaks %}
{% block dash_content %}
{{ block.super }}
{% url 'site_settings' %}
{% endblock %}
{% csrf_token %}

### signals
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from portal.utils import unique_slug_generator


    slug = models.SlugField()
    @property
    def title(self):
        return self.

@receiver(pre_save, sender=Company)
def company_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Address)
def address_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



ISSUE STATUS = [Open]
ISSUE TYPES = [Reports, FieldNote, ]
ASSET TYPES = [AGA, OD, Access]
ROLES = [Admin, Tech, Manager, User]

    {% if request.user.user_profile.role.pk == 'Admin' or request.user.user_profile.role.pk == 'Manager' %}







### LIST VIEW
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col"><a href="#">Company Name</a></th>
      <th scope="col"><a href="#">Contact</a></th>
      <th scope="col"><a href="#">Address</a></th>
      <th scope="col"><a href="#">Products</th>
      <th scope="col"><a href="#">Users</a></th>
    </tr>
  </thead>
  <tbody>
  {% for company in object_list %}
    <tr class='clickable-row' data-href='{{ company.get_absolute_url }}'>
      <th scope="row">{{ company.name }}</th>
      <td>{{ company.contact.fullname }}</td>
      <td>{{ company.address.street }}</td>
      <td>153</td>
      <td>12</td>
    </tr>

  {% endfor %}
  </tbody>
  <tfoot>
    <tr>
      <th scope="col" colspan="6" align="right">
        <a href="{% url 'organizations:company_create' %}"
            class="btn  btn-primary">Add Company</a>
      </th>
    </tr>
  </tfoot>
</table>



### DETAIL VIEW
<div class="col-md-10">
    <div class="card">
        <div class="card-header bg-light">{{company.name}}</div>

        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <div>Contact: <span class="text-muted small">{{ company.contact.fullname }}</span></div>
                    <div>Descripton:</div>
                    <div class="text-muted small">{{ company.description }}</div>
                </div>

                <div class="col-md-6">
                    <div>Address:</div>
                    <div>Street: <span class="text_muted small">{{ company.address.street }}</span></div>
                    <div>Street: <span class="text_muted small">{{ company.address.street2 }}</span></div>
                    <div>City: <span class="text_muted small">{{ company.address.city }}</span></div>
                    <div>Province: <span class="text_muted small">{{ company.address.province }}</span></div>
                    <div>Postal Code: <span class="text_muted small">{{ company.address.postalcode }}</span></div>
                    <div>Country: <span class="text_muted small">{{ company.address.country }}</span></div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12"><span class="text-muted small">Last Updated: {{ company.updated }}</span></div>
        </div>

        <div class="card-footer bg-light text-right">
            <a href='{% url "organizations:company_edit" company.slug %}' class="btn btn-primary">Edit</a>
        </div>
    </div>
</div>
