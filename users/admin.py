""" User admin Classes"""
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from users.models import Profile

# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  """ Profile Admin """

  list_display = ('pk','user','phone_number','website','picture')

  list_display_links = ('user',)

  list_editable = ('website','phone_number')

  search_fields = ('user__email'
                  ,'user__username'
                  ,'user__first_name'
                  ,'user__last_name'
                  ,'phone_number')


  list_filter = ('created','modified','user__is_active','user__is_staff')

  fieldsets = (
      ('Profile', {
          "fields": (
            ('user', 'picture'), #si es una tupla se despliegan horizontalmente , si es un campo se despliega verticalmente

          ),
      }),
      ('Extra info',{
        'fields': (
          ('website','phone_number'),
          ('biography')

          
        )
      }),      
      ('Metadata',{
        'fields':(
          ('created','modified'),
        )
      })
  )

  readonly_fields = ( 'created', 'modified')
  

class ProfileInline(admin.StackedInline):
  """ Profile inline admin for user"""
  model = Profile
  can_delete = False
  verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
  """Add profile admin to base user admin"""
  inlines = (ProfileInline,)
  list_display = (
    'username',
    'email',
    'first_name',
    'last_name',
    'is_active',
    'is_staff'
  )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
