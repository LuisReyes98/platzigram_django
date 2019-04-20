""" User views"""
# to see how to create a custom login https://docs.djangoproject.com/en/2.2/topics/auth/default/#authentication-in-web-requests

#Django
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


#Views
from django.views.generic.detail import DetailView
from django.views.generic import FormView , UpdateView

#Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#Exceptions
from django.db.utils import IntegrityError

# Forms
from users.forms import SignupForm
# from users.forms import ProfileForm, SignupForm

class LoginView(auth_views.LoginView):
  """Login View"""
  template_name = 'users/login.html'
  redirect_authenticated_user = True


# Create your views here.

# def login_view(request):
#   # Login View
#   if request.method == 'POST':

#     username = request.POST['username']
#     password = request.POST['password']
    
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       login(request, user)
#       # Redirect to a success page.
#       return redirect('posts:feed')
#     else:
#       # Return an 'invalid login' error message.
#       return render(request, 'users/login.html',{'error':'Invalid username and password'})

#   return render(request,'users/login.html')


# Registrar con clase
class SignupView(FormView):
  """ Users signup view """
  template_name = "users/signup.html"
  form_class = SignupForm
  success_url = reverse_lazy('users:login')
  
  def form_valid(self,form):
    form.save()
    return super().form_valid(form)

# Registrar con metodo
# def signup(request):
#   """Signup View"""

#   # import pdb; pdb.set_trace()
#   if request.method == 'POST':
#     form = SignupForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('users:login')
#   else:
#     form = SignupForm()

#   return render(
#     request= request, 
#     template_name='users/signup.html',
#     context={
#       'form':form
#     },
#     )


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
  """Log out view"""
  template_name = "users/loggout.html"

@login_required
def logout_view(request):
  """Logout de un user"""
  logout(request)
  return redirect('users:login')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
  """Update profile view"""
  model = Profile
  template_name = "users/update_profile.html"
  fields = ['website', 'biography', 'phone_number', 'picture']

  def get_object(self):
    """Return user's profile """
    return self.request.user.profile

  def get_success_url(self):
    """Return to user's profile"""
    username = self.object.user.username
    return reverse('users:detail', kwargs={'username': username})



# @login_required
# def update_profile(request):
#   """Update a user's profile view."""
#   profile = request.user.profile
  
#   if request.method == 'POST':
#     form = ProfileForm(request.POST,request.FILES)
#     if form.is_valid():
#       data = form.cleaned_data

#       profile.website = data['website']
#       profile.phone_number = data['phone_number']
#       profile.biography = data['biography']
#       profile.picture = data['picture']
#       profile.save()
    
#       url = reverse('users:detail', kwargs={'username': request.user.username})
#       return redirect(url)
#   else:
#     form = ProfileForm()
  
#   return render(
#     request = request,
#     template_name = 'users/update_profile.html',
#     context = {
#       'profile': profile,
#       'user': request.user,
#       'form': form,
#     }
#   )



# Class views
class UserDetailView(LoginRequiredMixin, DetailView):
  """USer detail view"""
  template_name = 'users/detail.html'
  slug_field = 'username'
  slug_url_kwarg = 'username' #mismo nombre que en el url
  queryset = User.objects.all()

  context_object_name = 'user'

  def get_context_data(self, **kwargs):
    """Add users posts to context"""
    context = super().get_context_data(**kwargs)
    user = self.get_object()
    context["posts"] = Post.objects.filter(user=user).order_by('-created')
    return context
  
