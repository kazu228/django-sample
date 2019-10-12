from django.urls import path

from .views import SampleTemplateView
from django.views.generic import TemplateView

urlpatterns = [
    path('sample', SampleTemplateView.as_view())
]
