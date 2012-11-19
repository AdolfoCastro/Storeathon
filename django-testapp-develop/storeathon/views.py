from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from storeathon.models import Tienda, Item, Categoria
from storeathon.forms import SignupForm, TiendaForm, ItemForm, CategoriaForm

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
			new_tienda.slug = slugify(form.cleaned_data['nombre'])
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
	return render(request, 'store/store.html',{
		'tienda': tienda
		})

@login_required
def item_new(request):
	if request.method =='POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			new_item = Item()
			new_item.nombre = form.cleaned_data['nombre']
			new_item.descripcion = form.cleaned_data['descripcion']
			new_item.precio = form.cleaned_data['precio']
			new_item.categoria = Categoria.objects.get(id=form.cleaned_data['categoria'])
			new_item.existencia = form.cleaned_data['existencia']
			new_item.tienda = Tienda.objects.get(id=form.cleaned_data['tienda'])
			new_item.slug = slugify(form.cleaned_data['nombre'])
			new_item.save()

			return HttpResponseRedirect('/item/' + new_item.slug)
	else:
		form = ItemForm()

	return render(request, 'items/new_item.html', {
		'form': form
		})

def item(request, slug):
	try:
		item = Item.objects.get(slug=slug)
	except Item.DoesNotExist:
		raise Http404
	return render(request, 'items/item.html', {
		'item': item
		})

@login_required
def categoria_new(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			new_categoria = Categoria()
			new_categoria.nombre = form.cleaned_data['nombre']
			new_categoria.slug = slugify(form.cleaned_data['nombre'])
			new_categoria.save()

			return HttpResponseRedirect('/categoria/list')
	else:
		form = CategoriaForm()

	return render(request, 'categoria/new_categoria.html', {
		'form': form
		})

def categoria_list(request):
	try:
		categorias = Categoria.objects.all()
	except Categoria.DoesNotExist:
		raise Http404

	return render(request, 'categoria/list_categoria.html', {
		'categorias': categorias
		})