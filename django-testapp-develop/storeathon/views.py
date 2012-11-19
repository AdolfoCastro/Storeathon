from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from storeathon.models import Tienda
from storeathon.forms import SignupForm, TiendaForm

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			new_user = User()
			new_user.username = form.cleaned_data['username']
			new_user.email = form.cleaned_data['email']
			new_user.first_name = form.cleaned_data['first_name']
			new_user.last_name = form.cleaned_data['last_name']
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()

			return HttpResponseRedirect('/home/')

	else:
		form = SignupForm()

	return render(request, 'registration/signup.html', {
		'form': form,
		})

@login_required
def tienda_new(request):
	if request.method == 'POST':
		form = TiendaForm(request.POST)
		if form.is_valid():
			new_tienda = Tienda()
			new_tienda.nombre = form.cleaned_data['nombre']
			new_tienda.descripcion = form.cleaned_data['descripcion']
			new_tienda.slug = slug = slugify(new_tienda.nombre)
			new_tienda.dueno = request.user
			new_tienda.save()

			return HttpResponseRedirect('/store/'+new_tienda.slug)

	else:
		form = TiendaForm()

	return render(request, 'store/new_store.html',{
		'form': form,
		})

def tienda(request, slug):
	try:
		tienda = Tienda.objects.get(slug=slug)
	except Tienda.DoesNotExist:
		raise Http404
	return render_to_response('store/store.html',{
		'tienda': tienda
		})