from django.shortcuts import render

def home(request):
    context = {
        "member_id": 1
    }
    return render(request, "home.html", context)
