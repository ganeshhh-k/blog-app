from django.shortcuts import render

posts = [
    {
        'author': 'user1',
        'title': 'Blog post 1',
        'content': 'First post Content',
        'date_posted': 'Aug 27 2026'
    },
    {
        'author': 'user2',
        'title': 'Blog post 2',
        'content': 'second post Content',
        'date_posted': 'Aug 28 2026'
    },
]

def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):

    return render(request, 'blog/about.html', {'title': 'about'})