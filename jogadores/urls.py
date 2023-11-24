from django.urls import path

from . import views

app_name = 'jogadores'
urlpatterns = [
    path('', views.JogadorListView.as_view(), name='index'),  # edite esta linha
    path('create/', views.create_jogador, name='create'),
    path('<int:jogador_id>/', views.detail_jogador,
         name='detail'),
    path('update/<int:jogador_id>/', views.update_jogador, name='update'),
    path('delete/<int:jogador_id>/', views.delete_jogador, name='delete'),
    path('<int:jogador_id>/review/', views.create_comentario, name='review'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categoryFilter/<int:pk>', views.CategoryFilterView.as_view(), name='categoryFilter')
]
