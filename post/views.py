from django.shortcuts import render

def post_index(request):
    return None

def post(request, post_id=None):
    return render(request, "post.html")
