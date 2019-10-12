from django.urls import path

from .views import SampleTemplateView, MyCreateView
from django.views.generic import TemplateView

urlpatterns = [
    path('sample', SampleTemplateView.as_view(), name='index'),
    path('sample/create', MyCreateView.as_view(), name='create'),
]

