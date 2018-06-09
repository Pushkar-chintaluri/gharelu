from django.shortcuts import render
from django.http import HttpResponse
from search.models import Ingredient
# Create your views here.
def index(request):
#    return HttpResponse("Hey Anandita!!")
    return render(request, 'search/index.html')


def predict(request,name):
    return HttpResponse(Ingredient.objects.filter(name_vc__startswith=name))
    
