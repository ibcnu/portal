from django import forms
from .models import Issue


class IssueCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # print('IssueCreateForm:ARGS: ', args)
        # print('IssueCreateForm:KWARGS: ', kwargs)
        # print('IssueCreateForm:USER: ', self)
        # print('IssueCreateForm:user: ', self)

    # def post(self):

    def save(self, commit=True, *args, **kwargs):
        instance = super(IssueCreateForm, self).save(commit=False)
        # print('IssueCreateForm:SAVE(): ')
        # print('IssueCreateForm:INSTANCE:', instance)
        # print('INSTANCE.asset', instance.asset)

        # print('user', self.request.user)
        # print('IssueCreateForm:ARGS:', args)
        # print('IssueCreateForm:KWARGS:', kwargs)
        return super(IssueCreateForm, self).save()  # commit)

    class Meta:
        model = Issue
        fields = [
            'title',
            'asset',
            'issuetype',
            'status',
            'description',
            'summary',
            'currentowner',
            'createdby',
            'slug',
        ]
        widgets = {
            'createdby': forms.HiddenInput(),
            'slug': forms.HiddenInput(),
        }
