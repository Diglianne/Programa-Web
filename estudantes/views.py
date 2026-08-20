from django.shortcuts import render
from django.http import HttpResponse

#-- o arquivo views onde definimos as nossas regras de negócios
#-- método/função para listagem 
#-- de estudantes
def listarEstudantes(request):
    return HttpResponse('<h2>Olá estudantes, esta é a listagem</h2>')


def editarEstudantes(request):
    return HttpResponse('<h2>Editando o estudante fulano de tal</h2>')