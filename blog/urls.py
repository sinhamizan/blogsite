from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.Home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<name>', views.profile, name='user_profile'),
    path('about-myself/<name>', views.about_myself, name='about_myself'),
    path('about-me', views.about_me, name='about_me'),
    path('contact-me', views.contact_me, name='contact_me'),
    path('success', views.success, name='success'),
    path('search-result', views.Search, name='search'),
    path('post-detail/<int:id>', views.post_detail, name='post_detail'),
    path('category/<name>', views.post_category, name='post_category'),
    path('add-post', views.add_post, name='add_post'),
]