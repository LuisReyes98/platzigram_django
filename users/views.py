""" User views"""
# to see how to create a custom login https://docs.djangoproject.com/en/2.2/topics/auth/default/#authentication-in-web-requests

#Django
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
  # Login View
  if request.method == 'POST':

    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      # Redirect to a success page.
      return redirect('feed')
    else:
      # Return an 'invalid login' error message.
      return render(request, 'users/login.html',{'error':'Invalid username and password'})

  return render(request,'users/login.html')


@login_required
def logout_view(request):
  """Logout de un user"""
  logout(request)
  return redirect('login')
