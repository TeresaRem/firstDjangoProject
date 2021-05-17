from django.shortcuts import render, HttpResponse , HttpResponseRedirect
    
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return HttpResponseRedirect("/")

def show(request,number):
    print(f"the blog number is {number}")
    return HttpResponse(f"<h3>placeholder to display blog number  {number}</h3>")

def edit(request,number):
    return HttpResponse(f"<h2>placeholder to edit blog {number} </h3>")

def destroy(request,number):
    return HttpResponseRedirect("/")

#def destroy(request):
 #   return HttpResponseRedirect("/")


