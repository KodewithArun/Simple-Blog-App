from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})



def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            title=title,    
            content=content
        )

        return redirect('home')

    return render(request, 'create_post.html')


def post_details(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'post_detail.html',{'post':post})

def delete_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('home')


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect('home')

    return render(request, 'edit_post.html', {'post': post})

