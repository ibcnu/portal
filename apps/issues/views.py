from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import IssueCreateForm
from .models import Issue
from apps.comments.forms import CommentForm


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
    form = CommentForm

    def form_valid(self):
        print(self.form.cleaned_data)
        return super('AssetCreateView: ', self).form_valid(self.form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        issue = kwargs.get('object')

        initial_data = {
            'content_type': issue.get_content_type,
            'object_id': issue.id
        }
        self.form = CommentForm(self.request.POST or None, initial=initial_data)
        context['page_title'] = 'Issue Detail'
        context['users'] = issue.asset.users.all()
        context['comment_form'] = self.form
        # print(context)
        return context


class IssueCreateView(LoginRequiredMixin, CreateView):
    form_class = IssueCreateForm
    template_name = 'issues/issue_form.html'

    def form_valid(self, form):
        print('IssueCreateView:form_valid()')
        return super(IssueCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print('IssueCreateView: ')
        context['page_title'] = 'Create Issue'
        context['pid'] = self.request.GET['pid']
        context['current_user'] = self.request.user.id
        # print('IssueCreateView:CONTEXT: ', context)
        return context


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    form_class = IssueCreateForm

    def post(self, form, *args, **kwargs):
        print('==========================================')
        print('IssueUpdateView:POST')
        form = IssueCreateForm(self.request.POST)
        if not form.is_valid():
            print('==========================================')
            print('IssueUpdateView:FORM_ERRORS: ', form.errors)
        else:
            print('IssueUpdateView:FORM_VALID!:')
        return super(IssueUpdateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        print('IssueUpdateView:form_valid()')
        print('IssueUpdateView:form_valid()')

        return super(IssueUpdateView, self).form_valid(form)

    def post(self, *args, **kwargs):
        # print('IssueUpdateView:post()')
        form = IssueCreateForm(self.request.POST)
        if not form.is_valid():
            # print('forms are invalid')
            print('IssueUpdateView:FORM_NOT_VALID: ', form.errors)

        return super(IssueUpdateView, self).post(args, kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(context)
        context['page_title'] = 'Update Issue'
        context['current_user'] = self.request.user.id
        return context

    def get_queryset(self):
        return Issue.objects.all()
