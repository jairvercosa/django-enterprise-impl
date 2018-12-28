from django.views.generic import TemplateView


class SummaryView(TemplateView):
    template_name = 'core/summary.html'
