from django.shortcuts import render

def user_index(request):
    return render(request, "user_index.html")

def user_profile(request, member_id=None):
    return render(request, "")
