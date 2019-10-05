from django.urls import path

from .views import SampleTemplateView

urlpatterns = [
    path('sample/', SampleTemplateView.as_view()),
]
