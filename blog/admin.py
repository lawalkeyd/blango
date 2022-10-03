from django.contrib import admin
from blog.models import Tag, Post, Comment, AuthorProfile

# Register your models here.
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(AuthorProfile)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)