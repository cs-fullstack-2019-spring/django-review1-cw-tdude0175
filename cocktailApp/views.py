from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Cocktail
# Create your views here.
# this completes requirements for exercise two
def index(request):
    drinks = Cocktail.objects.all()
    content = \
        {
            'drinks':drinks
        }
    return render(request, 'cocktailApp/index.html',content)
def details(request, cocktailID):
    drink = get_object_or_404(Cocktail, pk = cocktailID)
    content = \
        {
            'drink':drink
        }

    return render(request, 'cocktailApp/details.html',content)


# this is work for exercise 1

pageIndex =\
    [
        {'pageID':1},
        {'pageID':2},
        {'pageID':3},
        {'pageID':4},
        {'pageId':5},
    ]

def home(request, lastpage):
    content =\
        {
            'lastpage':lastpage
        }
    return render(request, 'cocktailApp/Home.html',content)

def page2(request , lastpage):
    content =\
        {
            'lastpage': lastpage,
            'page': "page2"
        }
    print(lastpage)
    return render(request, 'cocktailApp/page2.html', content )

def page3(request , lastpage):
    content =\
        {
            'lastpage': lastpage
        }
    return render(request, 'cocktailApp/page3.html', content )

def page4(request ,lastpage):
    content =\
        {
            'lastpage': lastpage
        }
    return render(request, 'cocktailApp/page4.html', content )

def page5(request ,lastpage):
    content =\
        {
            'lastpage': lastpage
        }
    return render(request, 'cocktailApp/page5.html', content )