from django import forms
from storeathon.models import Tienda, Carrito, CarritoItem, Item, Categoria
from django.contrib.auth.models import User

class UserField(forms.CharField):
	def clean(self, value):
		super(UserField, self).clean(value)
		try:
			User.objects.get(username=value)
			raise forms.ValidationError("That username is taken.")
		except User.DoesNotExist:
			return value

class SignupForm(forms.Form):
	username = UserField(max_length=30)
	email = forms.EmailField(max_length=100)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput())
	password_conf = forms.CharField(widget=forms.PasswordInput(), label="Repeat your password")

	def clean_password(self):
		if self.data['password'] != self.data['password_conf']:
			raise forms.ValidationError('Passwords are not the same')
		return self.data['password']

	def clean(self,*args, **kwargs):
		self.clean_password()
		return super(SignupForm, self).clean(*args, **kwargs)

class TiendaField(forms.CharField):
	def clean(self, value):
		super(TiendaField, self).clean(value)
		try:
			Tienda.objects.get(nombre=value)
			raise forms.ValidationError("That name is taken.")
		except Tienda.DoesNotExist:
			return value

class TiendaForm(forms.Form):
	nombre = TiendaField(max_length=100)
	descripcion = forms.CharField(max_length=255, widget=forms.Textarea)

	def clean(self,*args, **kwargs):
		return super(TiendaForm, self).clean(*args, **kwargs)

class ItemField(forms.CharField):
	def clean(self, value):
		super(ItemField, self).clean(value)
		try:
			Item.objects.get(nombre=value)
			raise forms.ValidationError("That item already exists.")
		except Item.DoesNotExist:
			return value

class ItemForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	descripcion = forms.CharField(max_length=255)
	precio = forms.DecimalField(max_digits=10, decimal_places=2)
	categoria = forms.ChoiceField(choices=[(categoria.id, categoria.nombre) for categoria in Categoria.objects.all()], widget=forms.Select(attrs={'class':'ddl'}))
	existencia = forms.IntegerField()
	tienda = forms.ChoiceField(choices=[(tienda.id, tienda.nombre) for tienda in Tienda.objects.all()], widget=forms.Select(attrs={'class':'ddl'}))

	def save(self, tienda, commit = True):
		item = super(ItemForm, self).save(commit = False)
		item.tienda = tienda

		if commit:
			item.save()
		return item

class CategoriaField(forms.CharField):
	def clean(self, value):
		super(CategoriaField, self).clean(value)
		try:
			Categoria.objects.get(nombre=value)
			raise forms.ValidationError("That category already exists.")
		except Categoria.DoesNotExist:
			return value

class CategoriaForm(forms.Form):
	nombre = CategoriaField(max_length=100)

	def clean(self, *args, **kwargs):
		return super(CategoriaForm, self).clean(*args, **kwargs)

class CarritoItemForm(forms.ModelForm):
	pass