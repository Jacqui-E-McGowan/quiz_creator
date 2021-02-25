from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('new', views.new),
    path('create', views.create),
    path('dashboard/<int:quiz_id>/questions', views.questions),
    path('dashboard/<int:quiz_id>/add', views.add),
    path('dashboard/<int:quiz_id>/edit', views.edit),
    path('dashboard/<int:quiz_id>/update', views.update),
    path('dashboard/<int:quiz_id>/edit_questions', views.edit_questions),
    path('dashboard/<int:quiz_id>/update_questions', views.update_questions),
    path('dashboard/<int:quiz_id>/view', views.view),
    path('dashboard/<int:quiz_id>/participants', views.participants),
    path('dashboard/<int:quiz_id>/delete', views.delete),
    path('logout', views.logout),
]