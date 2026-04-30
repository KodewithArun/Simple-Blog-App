from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import Post , Comment
from .forms import PostForm

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'welcome.html')
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )

        return redirect('home')

    return render(request, 'create_post.html')


def post_details(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'post_detail.html',{'post':post})

@login_required
@login_required
def delete_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('home')


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect('home')

    return render(request, 'edit_post.html', {'post': post})


# like and dislike the post 

@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('home')

# Comment the post 

@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        text = request.POST.get("text")

        Comment.objects.create(
            post=post,
            user=request.user,
            text=text
        )

    return redirect('detail', id=id)
