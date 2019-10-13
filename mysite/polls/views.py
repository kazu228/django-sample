from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Person
from .forms import PersonForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .forms import FindForm

# Create your views here.

def find(request):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        str = request.POST['find']
        sql = 'select * from polls_person'
        if (str != ''):
            sql += ' where ' + str
        data = Person.objects.raw(sql)
    else:
        form = FindForm()
        data = Person.objects.all()
    params = {
        'data': data,
        'form': form
    }
    return render(request, 'polls/find.html', params)

class SampleTemplateView(TemplateView):
    template_name = "polls/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Person.objects.all()
        # context["form"] = PersonForm()
        return context
    
    # def post(self, request):
    #     num = request.POST['id']
    #     item = Person.objects.get(id=num)
    #     params = {
    #         'data': [item],
    #         'form': PersonForm(request.POST)
    #     }
    #     return render(request, 'polls/index.html', params)
    
class MyCreateView(CreateView):  #CRUDのC
    template_name = "polls/create.html"
    model = Person
    fields = "__all__"
    success_url = "/polls/sample"

class MyUpdateView(UpdateView):  #CRUDのU
    template_name = "polls/edit.html"
    model = Person
    fields = "__all__"
    success_url = "/polls/sample"
    
class MyDeleteView(DeleteView):  #CRUDのD
    template_name = "polls/delete.html"
    model = Person
    success_url = '/polls/sample'
    