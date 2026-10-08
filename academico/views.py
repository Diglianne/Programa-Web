from django.shortcuts import render, redirect

from academico.models import Curso, Disciplina, Professor, Turma
from estudantes.models import Estudante
from academico.models import Professor

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
    if request.method == "POST":
        # Captura os dados enviados pelos campos do formulário HTML
        matricula = request.POST.get('matricula')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        senha = request.POST.get('senha')
        foto = request.FILES.get('foto') # Para arquivos/fotos

        # Cria e salva o professor no banco de dados
        Professor.objects.create(
            matricula=matricula,
            nome=nome,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            senha=senha,
            foto=foto
        )
        # Redireciona de volta para a lista de professores após salvar
        return redirect('listarProfessores') 

    # Se for uma requisição GET, apenas mostra a página de cadastro
    return render(request, 'professores/adicionar.html')

def deletarProfessor(request, id):
    professor = Professor.objects.get(id=id)
    professor.delete()
    return redirect('listarProfessores')

def atualizarProfessor(request, id):
    # Lógica de atualização (podemos fazer depois se quiser)
    return render(request, 'professores/adicionar.html')


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