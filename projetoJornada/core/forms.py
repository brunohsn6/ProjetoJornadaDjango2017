from django import forms
from .models import Curso, Aluno
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class MatriculaModelForm(forms.ModelForm):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Aluno
		fields = ['nome', 'cpf', 'curso', 'data_de_nascimento', 'email', 'password', 'foto']

	def clean(self):
		data = super(MatriculaModelForm, self).clean()
		if(User.objects.filter(username = data.get('email')).count() > 0):
			raise ValidationError('Este usuário ja esta em uso!', code = 'invalid_username')
		
		return data

	def save(self, *args, **kwargs):
		user = User.objects.create_user(self.cleaned_data.get('email'), self.cleaned_data.get('email'), self.cleaned_data.get('password'))
		self.instance.user = user
		self.instance.score = 5
		self.instance.media = 5

		return super(MatriculaModelForm, self).save()

class LoginForm(forms.Form):
	email = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())