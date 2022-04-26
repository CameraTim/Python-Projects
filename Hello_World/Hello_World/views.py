from django.http import HttpResponse
from django.shortcuts import render


def helloMessage(request):
    users = ["Tim", "Bob", "Stephanie", "Elijah", "Gianna"]
    user_check = {
        'users': users,
    }
    return render(request, "home.html", user_check)