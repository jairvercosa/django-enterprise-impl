from django.urls import path

from .views.register_view import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
