from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'blog/home.html')

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def sala(request):
    return render(request,'blog/sala.html')

def post(request):
    return render(request,'blog/post.html')

def contact(request):
    return render(request,'blog/contact.html')