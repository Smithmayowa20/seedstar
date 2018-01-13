from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponseRedirect

from .models import Users
from .forms import UserForm

def index(request):
    return render(request, 'index.html')

	
def list_users(request):
    users = Users.objects.order_by('-created_at').all()
    context = {'users': users}
    return render(request, 'users_list.html', context)


def add_user(request):
	form_class = UserForm
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect('list_users',)
	else:
		form = form_class()
	return render(request, 'add_user.html', {'form': form,})