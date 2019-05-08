from django.shortcuts import render

posts = [
    {
        'author': 'NoahT',
        'title': 'Learning Django',
        'content': 'first test',
        'date_posted': 'August 25, 2019'
    },
    {
        'author': 'NoahT',
        'title': 'L Django',
        'content': 'Second',
        'date_posted': 'August 252, 2019'
    }
    
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html', {'title': 'About'})

