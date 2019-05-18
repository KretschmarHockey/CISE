from django.shortcuts import render
from django.views.generic import ListView
from .models import ItemDescription
from django.db.models import Q
from functools import reduce

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


def search_for_tree(keywords, filters):
    if keywords == '':
        return []
    queries = [Q(name__contains=kw) for kw in keywords.split()]
    filter_query = Q(item_type=filters)
    query = reduce(lambda curr, new: curr | new, queries)
    query_set = ItemDescription.objects.filter(query)
    return query_set if filters == 'none' else query_set.filter(filter_query)
