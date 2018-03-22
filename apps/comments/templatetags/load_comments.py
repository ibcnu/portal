from apps.comments.models import Comment
from django import template

register = template.Library()


@register.inclusion_tag('comments/load_comments.html')
def load_comments(url):
    qs = Comment.objects.filter(url=url)
    return {'comments': qs}
