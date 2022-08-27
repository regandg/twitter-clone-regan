from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())    



        # If the form is valid
        # Yes , Save
        # Redirect to Home

        # No, Show Error


    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]
    form = PostForm()
    #show
    return render(request, 'posts.html', 
                {'posts': posts})

def delete(request, post_id):
    # Find user
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

   #  output = 'POST ID is ' + str(post_id)
   # return HttpResponse(output)

def likes(request, post_id):
    likedtweet = Post.objects.get(id = post_id)
    likedtweet.like += 1
    likedtweet.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post=Post.objects.get(id=post_id)
    if request.method == "GET":
        posts = Post.objects.get(id=post_id)
        return render(request, 'edit.html', {"posts":posts})

    if request.method == "POST":
        editposts = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=editposts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")