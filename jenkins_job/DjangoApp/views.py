from django.shortcuts import render
from .models import MyModel
from .forms import MyModelForm
from django.http import HttpResponseRedirect

# Create your views here.

def djangoapp_list(request):
	mytables = MyModel.objects.all()
	return render(request, 'DjangoApp/DjangoApp_list.html', {'mytable': mytables})

def djangoapp_welcome(request):
	return render(request, 'DjangoApp/DjangoApp_welcome.html', {})

def djangoapp_add(request):
	if request.POST:
		form = MyModelForm(request.POST)
		if form.is_valid():
			MyModel = form.save(commit=False)
			# set some fields
			MyModel.save()
			# redirect
			return HttpResponseRedirect('/list/')
	else:
		form = MyModelForm()
	return render(request, 'DjangoApp/DjangoApp_add.html', {'form':form})