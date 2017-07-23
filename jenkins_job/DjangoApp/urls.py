from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$', views.djangoapp_welcome, name='welcome'),
	url(r'^list/', views.djangoapp_list, name='list'),
	url(r'^add/', views.djangoapp_add, name='add')
]