from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Jogador, Review, List, Provider, Category
from .forms import JogadorForm, ReviewForm, ProviderForm


class ListListView(generic.ListView):
    model = List
    template_name = 'jogadores/lists.html'


class ListCreateView(generic.CreateView):
    model = List
    template_name = 'jogadores/create_list.html'
    fields = ['name', 'author', 'jogadores']
    success_url = reverse_lazy('jogadores:lists')

class JogadorListView(generic.ListView):
    model = Jogador
    template_name = 'jogadores/index.html'

def list_jogadores(request):
    jogador_list = Jogador.objects.all()
    context = {'jogador_list': jogador_list}
    return render(request, 'jogadores/index.html', context)


def detail_jogador(request, jogador_id):
    jogador = get_object_or_404(Jogador, pk=jogador_id)
    context = {'jogador': jogador}
    return render(request, 'jogadores/detail.html', context)


def create_jogador(request):
    if request.method == 'POST':
        jogador_form = JogadorForm(request.POST)
        if jogador_form.is_valid():
            # Certifique-se de que o campo release_year está presente no formulário
            # Isso pode ser feito automaticamente se você estiver usando o ModelForm corretamente
            jogador = jogador_form.save(commit=False)

            # Certifique-se de que release_year está definido antes de salvar
            jogador.release_year = 2023  # Substitua isso pelo valor desejado

            jogador.save()

            # O método save_m2m() é usado para salvar os campos ManyToMany após salvar o objeto principal
            jogador_form.save_m2m()

            return HttpResponseRedirect(reverse('jogadores:detail', args=(jogador.pk,)))

    else:
        jogador_form = JogadorForm()

    context = {'jogador_form': jogador_form}
    return render(request, 'jogadores/create.html', context)

def update_jogador(request, jogador_id):
    jogador = get_object_or_404(Jogador, pk=jogador_id)

    if request.method == "POST":
        form = JogadorForm(request.POST)
        if form.is_valid():
            jogador.name = form.cleaned_data['name']
            jogador.poster_url = form.cleaned_data['poster_url']
            jogador.save()
            return HttpResponseRedirect(
                reverse('jogadores:detail', args=(jogador.id, )))
    else:
        form = JogadorForm(
            initial={
                'name': jogador.name,
                'poster_url': jogador.poster_url
            })

    context = {'jogador': jogador, 'form': form}
    return render(request, 'jogadores/update.html', context)

def delete_jogador(request, jogador_id):
    jogador = get_object_or_404(Jogador, pk=jogador_id)

    if request.method == "POST":
        jogador.delete()
        return HttpResponseRedirect(reverse('jogadores:index'))

    context = {'jogador': jogador}
    return render(request, 'jogadores/delete.html', context)

def create_comentario(request, jogador_id):
    jogador = get_object_or_404(Jogador, pk=jogador_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = form.cleaned_data['author']
            review_text = form.cleaned_data['text']
            review = Review(author=review_author,
                            text=review_text,
                            jogador=jogador)
            review.save()
            return HttpResponseRedirect(
                reverse('jogadores:detail', args=(jogador_id, )))
    else:
        form = ReviewForm()
    context = {'form': form, 'jogador': jogador}
    return render(request, 'jogadores/review.html', context)


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'jogadores/categories.html'

class CategoryFilterView(generic.DetailView):
    model = Category
    template_name = 'jogadores/categoryFilter.html'