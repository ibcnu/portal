from apps.comments.models import Comment
from django import template

register = template.Library()


@register.inclusion_tag('comments/load_comments.html')
def load_comments(instance):
    print('load_comments: ', instance)
    qs = Comment.objects.for_instance(instance)
    return {'comments': qs}
