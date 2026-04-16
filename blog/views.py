from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


posts = [
        {
        'author':'Arvind',
        'title':'Blog Post 1',
        'content':'First cntent',
        'date-posted':'16 April 2026 ',
        },
        {
        'author':'Yuvaan',
        'title':'Blog Post 2',
        'content':'Second cntent',
        'date-posted':'16 April 2026 ',
        }
]
def home(request):
    content = {
        'posts':posts
    }
    return render(request,'blog/home.html',content)


def about(request):
    return render(request, 'blog/about.html')