from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Person
# Create your views here.

class SampleTemplateView(TemplateView):
    template_name = "polls/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Person.objects.all()
        return context