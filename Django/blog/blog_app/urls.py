from django.urls import path
from .views import index, post, create_post, sign_up, sign_in, signout, my_posts

urlpatterns = [
    path("", index),
    path("post/<int:id>", post),
    path("create-post", create_post),
    path("signup", sign_up),
    path("signin", sign_in),
    path("logout", signout),
    path("my-posts", my_posts)
]


