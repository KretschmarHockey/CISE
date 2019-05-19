from .models import Tree
from django.db.models import Q
from functools import reduce


def get_filter_query(key, value):
    if key is 'type':
        return Q(type=value)
    elif key is 'soil':
        return Q(soil=value)
    elif key is 'sun':
        return Q(sun=value)
    elif key is 'food':
        return Q(food='food')
    elif key is 'water':
        return Q(water=value)
    elif key is 'pruning':
        return Q(pruning=value)
    elif key is 'height':
        ranges = value.split('-')
        if len(ranges) is 1:
            if ranges[0].contains('>'):
                query = Q(max_height__gte=ranges[0])
            else :
                query = Q(max_height__lte=ranges[0])
        else:
            query = Q(max_height__gte=ranges[0]) & Q(max_height__lte=ranges[1])
        return query
    elif key is 'growth_rate':
        return Q(growth_rate=value)
    elif key is 'price':
        return Q(price__lte=value)
    else:
        return Q(type='hedge')


def search_for_tree(keywords, filters):
    if keywords == '':
        return []
    queries = [Q(name__contains=kw) for kw in keywords.split()]
    query = reduce(lambda curr, new: curr | new, queries)
    query_set = Tree.objects.filter(query)
    if len(filters) is not 0:
        if 'price' in filters:
            filters['price'] = int(filters['price'])
        filter_list = [get_filter_query(key, value) for key, value in filters.items()]
        filter_query = reduce(lambda curr, new: curr & new, filter_list)
        query_set = query_set.filter(filter_query)

    return query_set
