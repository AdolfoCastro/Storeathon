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
	nombre = forms.CharField(max_length=100)
	descripcion = forms.CharField(max_length=255)

	def clean(self,*args, **kwargs):
		return super(TiendaForm, self).clean(*args, **kwargs)

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		exclude = ('tienda',)

	def save(self, tienda, commit = True):
		item = super(ItemForm, self).save(commit = False)
		item.tienda = tienda

		if commit:
			item.save()
		return item

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria

	def save(self, commit = True):
		categoria = super(CategoriaForm, self).save(commit = False)

		if commit:
			categoria.save()
		return categoria

class CarritoItemForm(forms.ModelForm):
	pass