from django.urls import path
from .views import index, post, create_post, sign_up, sign_in, signout, my_posts, my_profile, uplaods, Login
import blog_app.views

urlpatterns = [
    path("", index),
    path("post/<int:id>", post),
    path("create-post", create_post),
    path("signup", sign_up),
    path("signin", sign_in),
    path("logout", signout),
    path("my-posts", my_posts),
    path("profile", my_profile),
    path("upload", uplaods),
    path("set-session", blog_app.views.test_set_session),
    path("get-session", blog_app.views.test_get_session),
    path("query-test", blog_app.views.query_test),
    path("class-login", Login.as_view())
]


