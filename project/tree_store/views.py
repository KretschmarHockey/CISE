from django.shortcuts import render
from .models import TreeItem

# Create your views here.
def index(request):
    return render(request, 'tree_store/index.html')

def search_results(request):
    item_list = TreeItem.objects.all()
    return render(
        request, 
        'tree_store/search_results.html',
        {'results': item_list}
    )

def search(results):
    pass