from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
import numpy as np
import requests
from .forms import NameForm
import json
@csrf_protect
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            val = form.cleaned_data

            print(val)
            nome= val.get("your_name")
            print(nome)

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/search/'+nome)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'pesquisar.html')

def search (request,nome):
    r = requests.get("https://gameinfo.albiononline.com/api/gameinfo/search?q="+nome)
    #TODO uma lista mostrando os resultados para o usuario escolher, atualmente o sistema escolhe o primeiro
    #TODO é sem sentido colocar pra escolher entre guild e player

    x = r.json()
    print(x["players"][0].__class__.__name__)
    return render(request, 'search.html', {'lista_player': x["players"]})
def stats (request, contexto, nome):


    return render(request, 'pesquisar.html')