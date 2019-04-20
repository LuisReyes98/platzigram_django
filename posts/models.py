""" Posts model"""

# Django
from django.db import models

from django.contrib.auth.models import User

# Los models son la ORM de django
# ORM (Object Relational Mapper
# la ORM de ruby on rails es Active record

class Post(models.Model):
  """ Post Model"""
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  profile = models.ForeignKey('users.Profile', on_delete = models.CASCADE)

  title = models.CharField(max_length = 255)
  photo = models.ImageField(upload_to = 'posts/photos')
  created = models.DateTimeField( auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  def __str__(self):  
    """return title and username"""

    return f'{self.title} by @{self.user.username}'
