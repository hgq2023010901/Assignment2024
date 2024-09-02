from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("poems index.")
def details(request, poem_id):
    return HttpResponse("details page of {}".format(poem_id))
def delete(request, poem_id):
    return HttpResponse("delete page of {}".format(poem_id))
def add(request):
    return HttpResponse("add page")
def edit(request, poem_id):
    return HttpResponse("edit page of {}".format(poem_id))