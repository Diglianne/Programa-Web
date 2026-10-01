from django.shortcuts import render

from academico.models import Curso, Disciplina, Professor, Turma
from estudantes.models import Estudante

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def listarProfessores(request):
    #-- obtêm todas as instâncias com todos os registros
    #-- dos professores
    professores = Professor.objects.all()
    
    contexto = {
        'profs' : professores,
    }
    return render(request,'professores/listagem.html',contexto)

def criarProfessor(request):
    return render()

def deletarProfessor(request):
    return render()

def atualizarProfessor(request):
    return render()

def listarCursos(request):
    cursos = Curso.objects.all()
        
    contexto = {
        'listCursos' : cursos,
    }
    
    return render(request,'cursos/listagem.html',contexto)

def criarCurso(request):
    return render()

def deletarCurso(request):
    return render()

def atualizarCurso(request):
    return render()

def listarTurmas(request):
    turmas =  Turma.objects.all()
    dicionario = {
        'listaTurmas' : turmas
    }
    return render(request,'turmas/listagem.html', dicionario)

def criarTurma(request):
    return render()

def deletarTurma(request):
    return render()

def atualizarTurma(request):
    return render()

def listarDisciplinas(request):
    disciplinas =  Disciplina.objects.all()
    dicionario = {
        'listaDisciplinas' : disciplinas
    }
    return render(request,'turmas/listagem.html', dicionario)

def criarDisciplina(request):
    return render()

def deletarDisciplina(request):
    return render()

def atualizarDisciplina(request):
    return render()