from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.

from blango_auth.models import User

class BlangoUserAdmin(UserAdmin):
  fieldsets = (
      (None, {'fields': ('email', 'password')}),
      (_('Personal info'), {'fields': ('first_name', 'last_name')}),
      (_('Permissions'), {
          'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
      }),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ('email', 'first_name', 'last_name', 'is_staff')
  search_fields = ( 'first_name', 'last_name', 'email')
  ordering = ('email',)

admin.site.register(User, BlangoUserAdmin)

