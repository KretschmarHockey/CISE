from django.shortcuts import render
from django.views.generic import ListView
from .models import TreeItem
from django.db.models import Q
from functools import reduce

# Create your views here.
def index(request):
    return render(request, 'tree_store/index.html')

def search(request):
    return render(request, 'tree_store/search.html')

class SearchResultsView(ListView):
    template_name = 'tree_store/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        return search_for_tree(self.request.GET.get('search_input', ''))

def search_for_tree(keywords):
    if keywords == '':
        return []
    queries = [Q(name__contains=kw) for kw in keywords.split()]
    query = reduce(lambda curr, new: curr | new, queries)
    return TreeItem.objects.filter(query)