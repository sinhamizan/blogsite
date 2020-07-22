from django.contrib import admin
from .models import Post_Catetory, Post, Comment, ContactMe, RegisterUser

# Register your models here.

admin.site.register(Post)
admin.site.register(Post_Catetory)
admin.site.register(ContactMe)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active = True)

admin.site.register(RegisterUser)