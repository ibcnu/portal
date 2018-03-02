# from django.shortcuts import render
from django.views.generic import TemplateView


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class AssetListView(TemplateView):
    template_name = "assets/asset_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AssetListView, self).get_context_data(*args, **kwargs)
        context = {
            'page_title': 'Asset List',
        }
        return context
