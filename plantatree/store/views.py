from django.shortcuts import render
from django.views.generic import ListView
from .searching import search_for_tree

# Create your views here.


def search(request):
    return render(request, 'store/search.html')


class SearchResultsView(ListView):
    template_name = 'store/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        keywords = self.request.GET.get('search_input', '')
        filters = self.request.GET.get('type', '')
        return search_for_tree(keywords, filters)
