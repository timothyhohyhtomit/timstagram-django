from django.shortcuts import render

def user_index(request):
    return render(request, "user_index.html")

def user_profile(request, member_id=None):
    context = {
        "member_id": member_id
    }
    return render(request, "user_profile.html", context=context)
