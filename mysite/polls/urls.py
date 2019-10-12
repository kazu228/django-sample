from django.urls import path

from .views import SampleTemplateView, MyCreateView, MyUpdateView
from django.views.generic import TemplateView

urlpatterns = [
    path('sample', SampleTemplateView.as_view(), name='index'),
    path('sample/create', MyCreateView.as_view(), name='create'),
    path('sample/edit/<int:pk>', MyUpdateView.as_view(), name='edit')
]

