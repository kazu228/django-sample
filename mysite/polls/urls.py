from django.urls import path, re_path
# from django.conf.urls import url
from .views import SampleTemplateView, MyCreateView, MyUpdateView, MyDeleteView
#from django.views.generic import TemplateView

urlpatterns = [
    path('sample', SampleTemplateView.as_view(), name='index'),
    path('sample/create', MyCreateView.as_view(), name='create'),
    re_path('sample/edit/(?P<pk>\d+)$', MyUpdateView.as_view(), name='edit'),  #汎用viewでURLに値を渡すには、re_pathがいいかな？
    re_path('sample/delete/(?P<pk>\d+)$', MyDeleteView.as_view(), name='delete')
]

