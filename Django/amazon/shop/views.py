from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo, Person

# Create your views here.

my_list = [ 
    { "name": "John", "id": 50000}, 
    { "name": "Mark", "id": 25555}, 
    { "name": "Lewis", "id": 49999},
]


def index(request):
    return render(request, "shop/index.html")

def about(request):
    return render(request, "shop/about.html")


def shop_home(request):
    return render(request, "shop/home.html")

def shop_two(request):
    return render(request, 
                "shop/home.html", 
                { 
                    "name": "Jon Mark", 
                    "showText": False,
                    "products": ["Apple", "Banana", "Orange"],
                    "students": my_list
                })

def current_shop(request, name):
    return render(request, "shop/home.html", { })


def shop_two_number(request, number, name):
    print(type(number))
    return HttpResponse(name + str(number))

def shop_three_number(request, number, name):
    print(type(number))
    return HttpResponse("This 3")

def add_simple_todo(request):
    Todo.objects.create(activity = "Dancing Flying", point=300)
    return HttpResponse("Added")

def delete_simple_todo(request):
    todo = Todo.objects.get(id=3)
    todo.point = 200
    todo.activity = "Nothing"
    todo.save()
    return HttpResponse("Added")

def get_simple_todo(request):
    todos = Todo.objects.all()
    
    return render(request,"shop/todo-simple.html", {
        "todos": todos
    })
    