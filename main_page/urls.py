from django.urls import path
from .views import string_post_view, manga_detail_view

urlpatterns = [
    path('home_page/', string_post_view),
    path('manga_detail/<int:id>/', manga_detail_view),
]