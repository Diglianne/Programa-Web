from django.shortcuts import redirect, render
from django.http import HttpResponse

from estudantes.forms import EstudanteForm
from estudantes.models import Estudante

#-- o arquivo views onde definimos as nossas regras de negócios
#-- método/função para listagem 
#-- de estudantes



def editarEstudantes(request, id = None):
    estudante = Estudante.objects.get(pk = id)
    aluno = EstudanteForm(request.POST or None, request.FILES or None, instance = estudante)
    if aluno.is_valid():
            aluno.save()
            return redirect('/')

    dicionario = {
            'form' : aluno
        }
    
    return render(request, "editar.html", context = dicionario)

#-- regra de negócio para adicionar estudante
def criarEstudante(request):
    form = EstudanteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    

    dicionario = {
        'form' : form 
    }

    return render(request, "estudantes/adicionar.html", dicionario)

def listarEstudantes(request):
    estudante = Estudante.objects.all()
    contexto ={
        'estudantes' : estudante,
    }

    return render(request, 'estudantes/listagem.html', contexto)

def deletarEstudante(request, pk=None):
    estudante = Estudante.objects.get(id=pk)
    estudante.delete()
    return redirect('/')

def atualizarEstudante(request, pk):
    editar = Estudante.objects.get(pk=pk)

    edicao = EstudanteForm(request.POST or None, request.FILES or None, instance=editar)
    if edicao.is_valid():
        edicao.save()
        return redirect ('/')

    dicionario = {
     'form' : edicao
    }

    return render(request, 'estudantes/adicionar.html', context = dicionario)
