from django.shortcuts import render
from django.views.generic import ListView, DetailView

from store.models import Tree
from .searching import search_for_tree


# Create your views here.


def search(request):
    return render(request, 'store/search.html')


class SearchResultsView(ListView):
    template_name = 'store/search_results.html'
    context_object_name = 'results'
    filter_names = [
        'type',
        'soil',
        'sun',
        'food',
        'water',
        'pruning',
        'height',
        'growth',
        'price',
    ]

    def get_queryset(self):
        keywords = self.request.GET.get('search_input', '')
        filters = {
            x: self.request.GET.get(x, '')
            for x in self.filter_names
            if self.request.GET.get(x, '') is not '' and self.request.GET.get(x, '') != 'none'
        }
        return map(lambda s: ProductDisplay(s), search_for_tree(keywords, filters))


class ProductView(DetailView):
    model = Tree
    context_object_name = 'context'
    template_name = 'store/purchase.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ProductDisplay:
    def __init__(self, data) -> None:
        self.display = str(data)
        self.data = data
