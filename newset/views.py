from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def new_set(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
    else:
        return render(request, "newset/new.html")