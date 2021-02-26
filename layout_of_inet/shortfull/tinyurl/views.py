
# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .full_url_form import FullUrlForm

# Create your views here.
def index(request:HttpRequest):
    full_url_form = FullUrlForm()

    return  render(request,"index.html",{"url_form": full_url_form  })
