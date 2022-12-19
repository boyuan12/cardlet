from io import StringIO
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import FlashCard, Set
import helpers
import csv

# Create your views here.
@csrf_exempt
def new_set(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
        title = json_data["title"]
        json_data = json_data["data"]
        set = Set.objects.create(title=title, user=request.user, set_id=helpers.random_int())

        for i in range(len(json_data)):
            FlashCard.objects.create(order=i, word=json_data[i][0], definition=json_data[i][1], set=set)
        
        return JsonResponse({"redirect": f"/set/{set.set_id}"})
    else:
        return render(request, "newset/new.html")

def upload_set_via_csv(request):
    if request.method == "POST":
        f = request.FILES['file']
        file = f.read().decode('utf-8')
        title = request.POST["title"]
        csv_data = csv.reader(StringIO(file), delimiter=',')
        set = Set.objects.create(title=title, user=request.user, set_id=helpers.random_int())
        order = 0

        for row in csv_data:
            if row == ["key", "definition"]:
                continue
            FlashCard.objects.create(order=order, word=row[0], definition=row[1], set=set)
            order += 1

        return redirect(f"/set/{set.set_id}")
    else:
        return render(request, "newset/upload.html")