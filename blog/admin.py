from django.contrib import admin
from blog.models import Tag, Post, Comment

# Register your models here.
admin.site.register(Tag)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)