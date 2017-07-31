from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import Aluno
from .forms import MatriculaModelForm, LoginForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

#Funções e classes que são responsáveis por executar as ações requisitadas
def cadastro(request):
	form = MatriculaModelForm()
	msg = ""
	nome = ""
	if(request.method == 'POST'):
		form = MatriculaModelForm(request.POST, request.FILES)
		nome = request.POST.get('nome')
		if(form.is_valid()):
			form.save()
			form = MatriculaModelForm()
			msg = "Cadastro efetuado com sucesso!"

	return render(request, 'core/cadastro.html', {'form':form, 'nome':nome,'msg':msg})

def home(request):
	return render(request, 'core/home.html')
@login_required
def conta(request):
	return render(request, 'core/conta.html', {'user':request.user})

def logout(request):
	auth_logout(request)
	return redirect('/home')

def login(request):
	msg = ''
	if(request.method == 'POST'):
		form = LoginForm(request.POST)
		if(form.is_valid()):
			username = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if(user is not None):
				auth_login(request, user)
				return redirect('/cadastros')
			else:
				msg = 'Email ou senha Incorretos!'
				return render(request, 'core/login.html', {'form':form, 'msg':msg})
	form = LoginForm()
	return render(request, 'core/login.html', {'form':form})


class AlunoListView(ListView):
	model = Aluno

class AlunoDetailView(DetailView):
	model = Aluno