from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'news_list' : [
    {
    'title' : 'News 1',
    'category' : 'Politics',
    'postdate' : '27/3/2023',
    },
    {'title' : 'News 2',
    'category' : 'Business',
    'postdate' : '27/3/2023'}
]
    }
    return render(request, 'home.html', context)