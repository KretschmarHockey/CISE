from .models import ItemDescription
from django.db.models import Q
from functools import reduce


def search_for_tree(keywords, filters):
    if keywords == '':
        return []
    queries = [Q(name__contains=kw) for kw in keywords.split()]
    filter_query = Q(item_type=filters)
    query = reduce(lambda curr, new: curr | new, queries)
    query_set = ItemDescription.objects.filter(query)
    return query_set if filters == 'none' else query_set.filter(filter_query)
