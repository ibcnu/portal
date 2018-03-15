from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Issue
from .forms import IssueCreateForm


class IssueListView(LoginRequiredMixin, ListView):
    paginate_by = 5
    context_object_name = "issues"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Issue.objects.fitler(
                Q(title__iexact=slug) |
                Q(title__contains=slug)
            )
        else:
            queryset = Issue.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(IssueListView, self).get_context_data(*args, **kwargs)
        context['page_title'] = 'Issue List'
        return context


class IssueDetailView(LoginRequiredMixin, DetailView):
    queryset = Issue.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        issue = kwargs.get('object')
        context['page_title'] = 'Issue Detail'
        context['users'] = issue.asset.users.all()
        print(context)
        return context


class IssueCreateView(LoginRequiredMixin, CreateView):
    form_class = IssueCreateForm
    template_name = 'issues/issue_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Create Issue'
        return context


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    form_class = IssueCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Update Issue'
        return context

    def get_queryset(self):
        return Issue.objects.all()
