from apps.assets.models import Asset
from django import template
register = template.Library()


@register.inclusion_tag('assets/load_asset_list.html')
def load_asset_list(*args, **kwargs):
    assets = Asset.objects.all()
    return {'asset_list': assets}
