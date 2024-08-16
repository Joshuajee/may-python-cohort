from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", { "posts": posts })


def post(request, id):
    post = Post.objects.get(id=id)
    post.views += 1
    post.save()
    return render(request, "post.html", { "post": post })

def create_post(request):
    
    if request.method == "POST":
        
        title = request.POST['title']
        content = request.POST['content']
        
        Post.objects.create(user_id=1, title=title, content=content)
        
        return render(request, "create-post.html", {"success": "Post created successfully"})
    
    return render(request, "create-post.html")