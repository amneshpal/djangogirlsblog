

# Create your views here.
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def home(request):
    return render(request, 'blog/home.html', {})


def header(request):
    return render(request, 'blog/header.html', {})

def footer(request):
    return render(request, 'blog/footer.html', {})

