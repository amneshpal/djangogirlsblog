

# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def home(request):
    return render(request, 'home.html', {})


def header(request):
    return render(request, 'header.html', {})

def footer(request):
    return render(request, 'footer.html', {})

