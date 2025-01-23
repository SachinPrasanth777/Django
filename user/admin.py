from django.contrib import admin
from .models import Role, UserRole, Article

admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(Article)
