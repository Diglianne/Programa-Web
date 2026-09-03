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
def adicionarEstudante(request):
    form = EstudanteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    

    dicionario = {
        'form' : form 
    }

    return render(request, "adicionar.html", dicionario)

def listarEstudantes(request):
    estudantes = Estudante.objects.all()
    contexto ={
        'listaEst' : estudantes,
    }

    return render(request, 'listagem.html', contexto)

def deletarEstudante(request, id=None):
    estudante = Estudante.objects.get(pk=id)
    estudante.delete()
    return redirect('/')



