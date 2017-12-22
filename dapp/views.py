from django.views.generic import TemplateView, View
from braces.views import AjaxResponseMixin, JSONResponseMixin, CsrfExemptMixin

import requests
class IndexView(TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rg']  = range(30)
        return context


class DetailView(TemplateView):
    template_name = 'web/detail.html'

class LoginView(TemplateView):
    template_name = 'web/login.html'

class RegisterView(TemplateView):
    template_name = 'web/register.html'

class  DataHubView(CsrfExemptMixin, AjaxResponseMixin, JSONResponseMixin, View):
    def post(self, request, *args, **kwargs):
        return self.post_ajax(request, args, kwargs)

    def post_ajax(self, request, *args, **kwargs):
        # request_url = request.POST.get('url', None)
        return self.render_json_response(requests.get('https://www.okex.com/api/v1/kline.do?symbol=ltc_btc&type=1min').json())



