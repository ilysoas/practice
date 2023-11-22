from django.shortcuts import render, get_object_or_404
from .models import RunString, Manga, Afisha, Slider

def string_post_view(request):
    if request.method == 'GET':
        string_ = RunString.objects.all()
        manga_list = Manga.objects.all()
        afisha = Afisha.objects.all()
        slider = Slider.objects.all()
        return render(request, template_name='main_page/index.html',
                      context={
                          'string_': string_,
                          'manga_list': manga_list,
                          'afisha': afisha,
                          'slider_list': slider

                      })


def manga_detail_view(request, id):
    if request.method == 'GET':
        manga_id = get_object_or_404(Manga, id=id)
        return render(request, template_name='main_page/manga_detail.html', context={'manga_id': manga_id})
