# from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Comment
# from apps.issues.models import Issue
from .forms import CommentCreateForm


class CommentListView(LoginRequiredMixin, ListView):
    context_object_name = "comments"

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.all()
        # if self.request.user.user_profile.role.name != 'Admin':
        #     queryset = self.request.user.user_profile.assets.all()

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(CommentListView, self).get_context_data(*args, **kwargs)
        context['page_title'] = 'Comment List'
        # print(context)
        return context


class CommentDetailView(LoginRequiredMixin, DetailView):
    queryset = Comment.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Comment Detail'
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentCreateForm
    template_name = 'comments/comment_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'Create Comment'
        return context


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CommentCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_title'] = 'Update Comment'
        return context

    def get_queryset(self):
        return Comment.objects.all()
