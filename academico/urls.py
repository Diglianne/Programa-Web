from django.urls import path
from academico import views
from estudantes import views as estViews

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Professor
    path('professores', views.listarProfessores, name='professor_listar'),
    path('professores/novo/', views.criarProfessor, name='professor_criar'),
    path('professores/<int:pk>/editar/', views.atualizarProfessor, name='professor_atualizar'),
    path('professores/<int:pk>/deletar/', views.deletarProfessor, name='professor_deletar'),

    # Estudante
    path('estudantes/', estViews.listarEstudantes, name='estudante_listar'),
    path('estudantes/novo/', estViews.criarEstudante, name='estudante_criar'),
    path('estudantes/<int:pk>/editar/', estViews.atualizarEstudante, name='estudante_atualizar'),
    path('estudantes/<int:pk>/deletar/', estViews.deletarEstudante, name='estudante_deletar'),

    # Turma
    path('turmas/', views.listarTurmas, name='turma_listar'),
    path('turmas/novo/', views.criarTurma, name='turma_criar'),
    path('turmas/<int:pk>/editar/', views.atualizarTurma, name='turma_atualizar'),
    path('turmas/<int:pk>/deletar/', views.deletarTurma, name='turma_deletar'),

    # Disciplina
    path('disciplinas/', views.listarDisciplinas, name='disciplina_listar'),
    path('disciplinas/novo/', views.criarDisciplina, name='disciplina_criar'),
    path('disciplinas/<int:pk>/editar/', views.atualizarDisciplina, name='disciplina_atualizar'),
    path('disciplinas/<int:pk>/deletar/', views.deletarDisciplina, name='disciplina_deletar'),
    
    # Cursos
    path('cursos/', views.listarCursos, name='curso_listar'),
    path('cursos/novo/', views.criarCurso, name='curso_criar'),
    path('cursos/<int:pk>/editar/', views.atualizarCurso, name='curso_atualizar'),
    path('cursos/<int:pk>/deletar/', views.deletarCurso, name='curso_deletar'),
]