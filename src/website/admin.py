from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import *


class PostAdmin(admin.ModelAdmin):
    """Displays Setting objects in the Django admin interface."""
    list_display = ('title', 'user', 'posted')
    list_filter = ('user',)
    search_fields = ('title',)


admin_list = [
    (Post, PostAdmin),
]

[admin.site.register(*t) for t in admin_list]