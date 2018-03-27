from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .forms import IssueCreateForm
from .models import Issue
from apps.comments.forms import CommentForm
from apps.comments.models import Comment


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


def IssueDetailView(request, slug):
    template_name = 'issues/issue_detail.html'
    instance = get_object_or_404(Issue, slug=slug)

    # comments = instance.comments
    initial_data = {
        'content_type': instance.get_content_type,
        'object_id': instance.id,
        'user': request.user,
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        print(form.cleaned_data)
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get("content")
        title = form.cleaned_data.get("short_text")
        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            short_text=title
        )
    context = {
        'issue': instance,
        'page_title': 'Issue Detail',
        'comment_form': form,
    }
    return render(request, template_name, context)


# class IssueDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'issues/issue_detail.html'
#     queryset = Issue.objects.all()
#     form = CommentForm

#     def post(self, form, *args, **kwargs):
#         print('==========================================')
#         print('IssueDetailView:POST')
#         form = CommentForm(self.request.POST)
#         if not form.is_valid():
#             print('==========================================')
#             print('IssueDetailView:FORM_ERRORS: ', form.errors)
#         else:
#             print('IssueDetailView:FORM_VALID!:')

#         # context = self.get_context_data()
#         context = {}
#         return render(self.request, self.template_name, context)
#         # return super(IssueDetailView, self).post(request, *args, **kwargs)

#     def form_valid(self):
#         print(self.form.cleaned_data)
#         return super('AssetCreateView: ', self).form_valid(self.form)

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         # issue = kwargs.get('object')
#         print('KWARGS: ', kwargs)
#         initial_data = {}
#         # if issue:
#         #     initial_data = {
#         #         'content_type': issue.get_content_type,
#         #         'object_id': issue.id,
#         #         'user': self.request.user,
#         #     }
#         #     context['users'] = issue.asset.users.all()
#         self.form = CommentForm(self.request.POST or None, initial=initial_data)
#         context['page_title'] = 'Issue Detail'
#         context['comment_form'] = self.form
#         # print(context)
#         return context


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
        return super(IssueUpdateView, self).post(self.request, *args, **kwargs)

    def form_valid(self, form):
        print('IssueUpdateView:form_valid()')
        print('IssueUpdateView:form_valid()')

        return super(IssueUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(context)
        context['page_title'] = 'Update Issue'
        context['current_user'] = self.request.user.id
        return context

    def get_queryset(self):
        return Issue.objects.all()
