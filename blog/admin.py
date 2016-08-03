from django.contrib import admin
from blog.models import Post, Contact, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

admin.site.register(Post, PostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']

admin.site.register(Contact, ContactAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'message', 'author']

admin.site.register(Comment, CommentAdmin)
