from django.shortcuts import render
from movie.forms import Movieform
from movie.models import Moviemodel
# Create your views here.
def index_view(request):
    return render(request,'movie/index.html')

def add_movie_view(request):
    form=Movieform()
    if request.method=='POST':
        form=Movieform(request.POST)
        if form.is_valid():
            print('validation is sucessfull')
            form.save()
        return index_view(request)
    return render(request,'movie/addmovie.html',{'form':form})

def movie_list_view(request):
    movies_list=Moviemodel.objects.all()
    return render(request,'movie/listmovie.html',{'movies_list':movies_list})