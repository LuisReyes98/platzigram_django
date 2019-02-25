""" Post models """

from django.db import models

# Create your models here.
class User(models.Model):
  email = models.EmailField(unique = True)

  password = models.CharField(max_length = 100)

  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)

  bio = models.TextField(blank = True)

  birthdate = models.DateField(blank = True, null = True)

  created = models.DateTimeField(auto_now_add = True)
  modified = models.DateTimeField(auto_now = True)
    

  # class Meta:
  #   verbose_name = _("User")
  #   verbose_name_plural = _("Users")

  # def __str__(self):
  #   return self.name

  # def get_absolute_url(self):
  #   return reverse("User_detail", kwargs={"pk": self.pk})
