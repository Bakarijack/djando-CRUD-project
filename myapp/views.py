from django.shortcuts import render, get_object_or_404
from myapp.models import Flower

# Create your views here.
def index(request):
    flowers = Flower.objects.all()
    return render(request, "myapp/index.html", {'flowers': flowers})

def detail(request, slug=None):               #stores the slug from the url into the variable slug or None if the value is not passed into this parameter
    flower = get_object_or_404(Flower, slug=slug)         #stores the object with the slug into the variable flower if it is found, else it returns error 404
    return render(request, 'myapp/detail.html', {'flower': flower})