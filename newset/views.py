from ast import Pass
from django.shortcuts import render

# Create your views here.
def new_set(request):
    if request.method == "POST":
        pass

    else:
        return render(request, "newset/new.html")