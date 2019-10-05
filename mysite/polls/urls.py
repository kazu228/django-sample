from django.urls import path

from .views import SampleTemplateView

urlpatterns = [
    path(r'^sample$', SampleTemplateView.as_view()),
]
