from apps.assets.models import AssetType
from django import template
register = template.Library()


@register.inclusion_tag('assets/load_assettype_menu.html')
def load_assettype_menu(request):
    user = request.user
    assettypes = AssetType.objects.all()
    if user.user_profile.role.pk != 'Admin' and user.user_profile.role.pk != 'Tech':
        print(user.user_profile.company.assets.all().values_list('assettype', flat=True).distinct())
        # print(AssetType.objects.filter(user.company.assets.all()))
        assettypes = AssetType.objects.filter(name__in=user.user_profile.company.assets.all().values_list('assettype', flat=True).distinct())
    print(assettypes)
    return {'assettypes': assettypes}
