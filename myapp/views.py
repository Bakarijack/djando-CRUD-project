from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from myapp.models import Flower
from .forms import MyForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    #flowers = Flower.objects.all()
    q = request.GET.get('q', None)
    items = ''

    if q is None or q is '':
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains = q)
    return render(request, "myapp/index.html", {'flowers': flowers})

def detail(request, slug=None):               #stores the slug from the url into the variable slug or None if the value is not passed into this parameter
    flower = get_object_or_404(Flower, slug=slug)         #stores the object with the slug into the variable flower if it is found, else it returns error 404
    return render(request, 'myapp/detail.html', {'flower': flower})

def tags(request, slug=None):
    flowers = Flower.objects.filter(tags__slug = slug)
    return render(request, 'myapp/index.html',{'flowers': flowers})


def create(request):
   # context = {}
    if request.method == 'POST':
        form = MyForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = MyForm()

    #context['form'] = form  
    return render(request, 'myapp/create.html',{'form':form})

def edit(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == 'POST':
        form = MyForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)

    return render(request, 'myapp/edit.html',{'form':form})

def delete(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()

    return render(request, 'myapp/delete.html',{'flower':flower})