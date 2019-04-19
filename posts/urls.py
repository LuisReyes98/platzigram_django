"""Post URlS"""
from django.urls import path

#views 
from posts import views

urlpatterns = [
    # Posts
    path( route='', 
          view=views.PostsListView.as_view(),
          name='feed'
    ),  # root
    path( route="posts/new/", 
          view=views.create_post, 
          name='create'
    ),
]
