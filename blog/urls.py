from django.urls import path
from .views import starting_page, posts, post_detail

urlpatterns = [
    path("", starting_page, name='starting-page'),
    path("posts", posts, name='posts'),
    path("posts/<slug:slug>",post_detail, name='post-detail') # /post/my-first-post
]
