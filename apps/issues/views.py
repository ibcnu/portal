import os
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType

from .forms import IssueCreateForm
from .models import Issue
from apps.comments.forms import CommentForm
from apps.comments.models import Comment
from apps.files.forms import FileForm
from apps.files.models import File, FileAttachment


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

    print('==========================================')
    print('IssueDetailView: ', instance.files)
    # print('IssueDetailView: ', instance.fil/es[0].attachments.all)
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


# class AddFileView(LoginRequiredMixin, TemplateView):
#     template_name = 'issues/file-upload.html'

#     def post(self, request, *args, **kwargs):
#         context = self.get_context_data()
#         if context["form"].is_valid():
#             print(context["form"].cleaned_data)
#             print('yes done')
#             # save your model
#             # redirect
#         else:
#             print(context["form"].errors)

#         return super(AddFileView, self).render_to_response(context)

#     def function():
#         pass

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         # print(context)
#         context['page_title'] = 'Issue File Upload'
#         context['form'] = FileForm()
#         context['current_user'] = self.request.user.id
#         return context


def AddFileView(request, issue_pk):
    template_name = 'issues/file-upload.html'
    instance = get_object_or_404(Issue, pk=issue_pk)
    print('ISSUE_PK: ', issue_pk)
    print('INSTANCE: ', instance)

    initial_data = {
        'content_type': instance.get_content_type,
        'object_id': instance.id,
        'user': request.user,
    }
    form = FileForm(request.POST or None, request.FILES or None, initial=initial_data)
    if request.POST:
        if form.is_valid():
            print('AddFileView:FORM_DATA ', form.cleaned_data)
            c_type = form.cleaned_data.get("content_type")
            content_type = ContentType.objects.get(model=c_type)
            obj_id = form.cleaned_data.get('object_id')
            description = form.cleaned_data.get("description")

            title = form.cleaned_data.get("title")
            # filename_base, filename_ext = os.path.splitext(filename)

            files = request.FILES.getlist('myfiles')
            print('========================================')
            print('AddFileView:FORM_DATA:files  ', files)
            # print(files.count())
            print('========================================')

            parent_file = None
            counter = 0
            for a_file in files:
                if counter == 0:
                    # filename_base, filename_ext = os.path.splitext(a_file)
                    parent_file = File(
                        user=request.user,
                        content_type=content_type,
                        object_id=obj_id,
                        description=description,
                        title=a_file.name,
                        attachment=a_file,
                        # extension=filename_ext,
                    )
                    parent_file.save()
                else:
                    child = FileAttachment(
                        file=parent_file,
                        filename=a_file.name,
                        attachment=a_file,
                    )
                    child.save()
                counter += 1

            return redirect("issues:issue_details", instance.slug)
        else:
            print(form.errors)
    context = {
        'issue': instance,
        'page_title': 'Issue File Upload',
        'form': form,
    }
    return render(request, template_name, context)
