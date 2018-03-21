from django import template
register = template.Library()


@register.inclusion_tag('comments/load_comments.html')
def load_comments(issue):
    comments = issue.comments.all()
    return {'comments': comments}
