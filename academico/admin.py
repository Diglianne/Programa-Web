from django.contrib import admin
from academico.models import Professor, Departamento, Curso, Turma, Disciplina

# Register your models here.
class ProfessorAdmin(admin.ModelAdmin):
    list_display=('matricula', 'nome', 'email', 'cpf')

admin.site.register(Professor, ProfessorAdmin)

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display=('codigo', 'nome', 'imagem')

admin.site.register(Departamento, DepartamentoAdmin) # type: ignore

class CursoAdmin(admin.ModelAdmin):
    list_display=('codigo', 'nome', 'foto', 'duracao', 'data_inicio', 'cargaHoraria', 'departamento')

admin.site.register(Curso, CursoAdmin) # type: ignore

class TurmaAdmin(admin.ModelAdmin):
    list_display=('codigo', 'anoIngresso', 'periodo', 'curso')

admin.site.register(Turma, TurmaAdmin)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display=('codigo', 'nome', 'cargaHoraria', 'turno', 'turma', 'professor')

admin.site.register(Disciplina, DisciplinaAdmin)