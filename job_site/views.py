from django.shortcuts import render
from Chinese.models import Category, Food
from blog.models import Post
from bookmark.models import Bookmark
from photo.models import Album
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
    category = Category.objects.all()
    food = Food.objects.all()
    blog = Post.objects.all()
    bookmark = Bookmark.objects.all()
    album = Album.objects.all()
    context = {
        'category':category,
        'food':food,
        'blog': blog,
        'bookmark':bookmark,
        'album':album,
    }
    return render(request, 'home.html', context)


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html' 