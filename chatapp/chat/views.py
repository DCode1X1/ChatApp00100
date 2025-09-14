from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def room(request, room_name):
    return render(request, "chat/room.html", {
        "room_name": room_name,
        "username": request.user.username  # ✅ pass logged-in username
    })



def home(request):
    if request.user.is_authenticated:
        return render(request, "chat/home.html")
    return redirect("login")
