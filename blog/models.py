from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post_Catetory(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class RegisterUser(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=120)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    profile_picture = models.ImageField(default='avatar.png', blank=True)
    about_me  = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    category = models.ForeignKey(Post_Catetory, on_delete=models.CASCADE)
    description = RichTextField()
    author = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    is_approve = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=150)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class ContactMe(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

