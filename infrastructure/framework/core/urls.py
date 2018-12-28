from django.urls import path

from .views import SummaryView


urlpatterns = [
    path('', SummaryView.as_view(), name='summary'),
]
