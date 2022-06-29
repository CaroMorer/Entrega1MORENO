from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('cursos', views.cursos, name = 'Cursos'),
    path('profesores', views.profesores, name = 'Profesores'),
    path('estudiantes', views.estudiantes, name = 'Estudiantes'),
    path('entregables', views.entregables, name = 'Entregables'),
    path('curso_formulario', views.cursos, name = 'curso_formulario'),
    path('profesor_formulario', views.profesores, name = 'profesor_formulario'),
    path('buscar/', views.buscar),]