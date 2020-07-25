from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Post_Catetory, Post, ContactMe, RegisterUser
from django.db.models import Q 
from .forms import CommentForm, ContactForm, registerForm, newPostForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def Home(request):
    posts = Post.objects.all()
    # pagination
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts':page_obj,
    }
    template = 'index.html'
    return render(request, template, context)

    
def post_detail(request, id):
    # single post
    post = get_object_or_404(Post, id=id)
    # related post
    releted_posts = Post.objects.filter(category=post.category).exclude(id=id)[:4]
    # comment
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()


    context = {
        'post':post,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'releted_posts':releted_posts,
    }
    template = 'post_detail.html'
    return render(request, template, context)


def post_category(request, name):
    category = get_object_or_404(Post_Catetory, name=name)
    posts = Post.objects.filter(category=category)

    context = {
        'posts':posts,
    }
    template = 'post_category.html'
    return render(request, template, context)

    
def Search(request):
    posts = Post.objects.all()
    data = request.GET.get('q')
    if data:
        posts = posts.filter(
            Q(title__icontains=data) | 
            Q(description__icontains=data)
        )

    context = {
        'posts':posts,
        'total_posts':posts.count(),
        'data':data,
    }
    template = 'search.html'
    return render(request, template, context)


def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('blog:success')
    else:
        form=ContactForm()

    context = {
        'form':form,
    }
    template = 'contact_me.html'
    return render(request, template, context)

def success(request):
    template = 'success.html'
    return render(request, template)


def about_me(request):
    template = 'about_me.html'
    return render(request, template)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        auth = RegisterUser.objects.filter(username=username, password=password).first()
        if auth:
            request.session['userid'] = auth.id
            request.session['username'] = auth.username
            messages.success(request, 'Login Successfully.')
            return redirect('blog:home')
    template = 'login.html'
    return render(request, template)


def register(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        messages.info(request, 'Register SuccessFully Completed.')
        return redirect('blog:login')

    template = 'register.html'
    return render(request, template, {'form':form,})


def logout(request):
    request.session['userid'] = None
    request.session['username'] = None
    messages.warning(request, 'You are Logged Out.')
    return redirect('blog:login')

def profile(request, name):
    user = RegisterUser.objects.get(username=name)
    post = Post.objects.filter(author=user)

    context = {
        'user':user,
        'post':post,
        }
    template = 'profile.html'
    return render(request, template, context)


def about_myself(request, name):
    user = RegisterUser.objects.get(username=name)
    if request.method == 'POST':
        myself = request.POST['about_myself']
        user.about_me = myself
        user.save()
        messages.success(request, 'Successfully Added YourSelf.')
        return redirect('blog:user_profile', name=request.session.username)

    template = 'about_me.html'
    return render(request, template)


def add_post(request):
    user = get_object_or_404(RegisterUser, username=request.session['username'])
    form = newPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = user
        form.save()
        messages.success(request, 'Post Added Successfully.')
        return redirect('blog:home')

    template = 'add_post.html'
    return render(request, template, {'form':form,})









