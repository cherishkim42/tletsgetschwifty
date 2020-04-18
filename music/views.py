from django.shortcuts import render
from django.http import HttpResponse

from .models import Album, Song


def one_album(request, album_id):
    



def index(request):
    albums_list = Album.objects.order_by('-pub_date')
    context = {'albums_list': albums_list}
    return render(request, 'music/index.html', context)

# def one_album(request, album_name):
#     response = "This is the page for album %s"
#     return HttpResponse(response % album_name)