""" Platzigram user imafe middleware """

#Django
from django.shortcuts import redirect

from django.urls import reverse

class ProfileCompletitionMiddleWare:
  """Profile Completition MiddleWare 
    Ensure every user has profile picture and biography
    Redirecting them to chose one if they don't have one
  """

  def __init__(self,get_response):
    """Middleware initialization"""
    self.get_response = get_response



  def __call__(self,request):
    """Code to be executed for each request before the views is called"""

    if not request.user.is_anonymous:
      if not request.user.is_staff:
        profile = request.user.profile
        if not profile.picture or not profile.biography:
          if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
            return redirect('users:update_profile')    
    
    response = self.get_response(request)
    return response
