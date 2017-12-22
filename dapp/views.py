from django.views.generic import TemplateView


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
