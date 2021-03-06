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
        view=views.PostCreateView.as_view(), 
        name='create'
  ),
  #Posts
  path(
      route='post/<slug:username>/<int:pk>/',
      view=views.PostDetailView.as_view(),
      name='detail'
  )
]
