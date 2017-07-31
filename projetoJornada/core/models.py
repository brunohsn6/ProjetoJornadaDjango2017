from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

#classe que cadastra os cursos
class Curso(models.Model):
	nome = models.CharField(max_length=255)
	codigo = models.CharField(max_length=30)
	#função abaixo exibe alguns campos do cadastro na seção admin
	def __str__(self):
		return '{0} | {1}'.format(self.nome, self.codigo)
#classe que cadastra os alunos
class Aluno(models.Model):
	nome = models.CharField(max_length=255)
	cpf = models.CharField(max_length=14)
	codigo = models.CharField(max_length=30)
	curso = models.ForeignKey(Curso)
	score = models.DecimalField(default = 0, max_digits = 4, decimal_places = 2)
	media = models.DecimalField(default = 0, max_digits = 4, decimal_places = 2)
	data_de_nascimento = models.DateField()
	foto = models.ImageField()
	user = models.OneToOneField(settings.AUTH_USER_MODEL) #poderia ser usar também o "user" do import User!!
	#função abaixo exibe alguns campos do cadastro na seção admin
	def __str__(self):
		return '{0} | {1}'.format(self.nome, self.curso)

class Disciplina(models.Model):
	nome = models.CharField(max_length = 100)
	codigo_da_disciplina = models.CharField(max_length = 6)
	curso = models.ForeignKey(Curso)
	data_de_inserção = models.DateField(auto_now_add = True)
	eletiva = models.BooleanField(default = True)

	def __str__(self):
		if(self.eletiva == True):
			tipo = "Eletiva"
		else:
			tipo = "Não-Eletiva"

		return '{0} | {1} | {2}'.format(self.nome, '#'+self.codigo_da_disciplina, tipo)

