from django.db import models

from estudantes.models import Estudante

# Create your models here.
class Professor(models.Model):
    matricula = models.CharField(max_length=12)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    
class Departamento(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='fotos/cursos')


class Curso(models.Model):
    codigo = models.IntegerField(max_length=2, primary_key=True)
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/cursos')
    duracao = models.DecimalField(max_digits=3, decimal_places=2)
    data_inicio = models.DateField(blank=True, )
    cargaHoraria = models.IntegerField()
    professor = models.ManyToManyField(Professor, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
        
class Turma(models.Model):
    codigo = models.CharField(max_length=15)
    anoIngresso = models.IntegerField(max_length=4)
    periodo = models.IntegerField(max_length=1)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__(self):
        return self.codigo
    
class Disciplina(models.Model):
    codigo = models.IntegerField(max_length=3)
    nome = models.CharField(max_length=150)
    cargaHoraria = models.IntegerField()
    turno = models.CharField(max_length=10)
    turma = models.ForeignKey(Turma,on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)  
    estudante = models.ManyToManyField(Estudante, blank=True) 
    


# Create your models here.
