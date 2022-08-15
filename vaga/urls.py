from django.conf.urls import url 

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^quick_weigh$', views.quickWeigh, name='quickWeigh'),
	url(r'^detail_weigh$', views.detailWeigh, name='detailWeigh'),
]
