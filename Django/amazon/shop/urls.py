from django.urls import path
from .views import index, about, shop_home, shop_two, current_shop, add_simple_todo, get_simple_todo, delete_simple_todo

urlpatterns = [
    path("", index),
    path("about", about),
    path("home", shop_home),
    path("two", shop_two),
    path("<name>", current_shop),
    path("simple/add", add_simple_todo),
    path("simple/del", delete_simple_todo),
    path("simple/view", get_simple_todo)
    # path("two/<name>/status/<int:number>", shop_two_number),
    # path("two/<name>/status/<number>", shop_three_number)
]

