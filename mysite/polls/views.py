from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Person
from .forms import PersonForm
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

class SampleTemplateView(TemplateView):
    template_name = "polls/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Person.objects.all()
        context["form"] = PersonForm()
        return context
    
    def post(self, request):
        num = request.POST['id']
        item = Person.objects.get(id=num)
        params = {
            'data': [item],
            'form': PersonForm(request.POST)
        }
        return render(request, 'polls/index.html', params)
    
class MyCreateView(CreateView):  #CRUDのC
    template_name = "polls/create.html"
    model = Person
    fields = "__all__"
    success_url = "/polls/sample"

class MyUpdateView(UpdateView):  
    template_name = "polls/edit.html"
    model = Person
    fields = "__all__"
    success_url = "/polls/sample"
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)