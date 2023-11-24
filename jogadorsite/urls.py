from django.contrib import admin
from django.urls import include, path
 
urlpatterns = [
    path('', include('staticpages.urls')),
    path('jogadores/', include('jogadores.urls')), # adicionar esta linha
    path('admin/', admin.site.urls),
]   