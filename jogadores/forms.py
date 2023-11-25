
from .models import Jogador, Review
from .models import Jogador, Review, Provider
from django.forms import ModelForm


class JogadorForm(ModelForm):
    class Meta:
        model = Jogador
        fields = [
            'name',
            'poster_url',
            'categories',

        ]
        labels = {
            'name': 'Nome do Jogador',
            'poster_url': 'URL do Poster do Jogador',
            "categories": "categorias",

        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }

class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = [
        ]
        labels = {
        } 