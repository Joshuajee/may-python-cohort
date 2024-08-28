from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q
from django.views import View
from .models import Post, User
from .forms import SignUpForm, LoginForm

# Create your views here.

def index(request):
    q = request.GET.get("q", None)
    if q != None:
        posts = Post.objects.filter(title__icontains=q)
    else:
        posts = Post.objects.all()
    return render(request, "index.html", { "posts": posts, "q": q })


def post(request, id):
    post = Post.objects.get(id=id)
    post.views += 1
    post.save()
    return render(request, "post.html", { "post": post })

@login_required(login_url="/signin")
def my_profile(request):
    return render(request, "profile.html")

@login_required(login_url="/signin")
def my_posts(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, "index.html", { "posts": posts })


@login_required(login_url="/signin")
def create_post(request):
    user = request.user
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(user=user, title=title, content=content)
        return render(request, "create-post.html", {"success": "Post created successfully"})
    
    return render(request, "create-post.html")

def sign_up(request):   
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            username   = form.cleaned_data['username']
            email      = form.cleaned_data['email']
            password   = form.cleaned_data['password']
            
            try:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                return HttpResponseRedirect("/signin")
            except:
                return render(request, "signup.html", {"form": form})
                
    
    return render(request, "signup.html", {"form": form })

def sign_in(request):
    
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username   = form.cleaned_data['username']
            password   = form.cleaned_data['password']
            try: 
                user = authenticate(username = username, password=password)
                if user == None:
                    return render(request, "login.html", {"form": form, "error": "Invalid Details"})
                login(request, user)
                return HttpResponseRedirect("/")
            except:
                return render(request, "login.html", {"form": form})
                
    
    return render(request, "login.html", {"form": form })

def signout(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url="/signin")
def uplaods(request):
    
    user = User.objects.get(id=request.user.id)
    
    user.profile_image = request.FILES['image']
    
    user.save()
    
    return HttpResponseRedirect("/profile")



def test_set_session(request):
    request.session['name'] = "John Doe"
    
    return HttpResponse("Nothing")

def test_get_session(request):
    
    return HttpResponse(request.session['name'])


def query_test(request):
    name = request.GET['name']
    age = request.GET['age']
    print(name, age)
    return HttpResponse(name + " " + age)


class Login(View):
    
    def get(self, request):
        print("jjj")
        form = LoginForm()
        return render(request, "login.html", {"form": form })
    
    def post(self, request):
        print("post")
        form = LoginForm(request.POST)
        if form.is_valid():
            username   = form.cleaned_data['username']
            password   = form.cleaned_data['password']
            try: 
                user = authenticate(username = username, password=password)
                if user == None:
                    return render(request, "login.html", {"form": form, "error": "Invalid Details"})
                login(request, user)
                return HttpResponseRedirect("/")
            except:
                return render(request, "login.html", {"form": form})
                
    
