from django.urls import path
from .views import index, post, create_post

urlpatterns = [
    path("", index),
    path("post/<int:id>", post),
    path("create-post", create_post)
]


