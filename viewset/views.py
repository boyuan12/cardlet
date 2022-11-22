import json
from django.shortcuts import render
from newset.models import Set, FlashCard
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def view_set(request, set_id):
    set = Set.objects.get(set_id=set_id)
    flashcards = FlashCard.objects.filter(set=set)
    return render(request, "viewset/set.html", {
        "set": set,
        "flashcards": flashcards
    })

def view_set_json(request, set_id):
    set = Set.objects.get(set_id=set_id)
    flashcards = FlashCard.objects.filter(set=set, order=request.GET.get("order"))
    flashcards_json = serializers.serialize('json', flashcards)
    
    flashcards_json = json.loads(flashcards_json)
    return JsonResponse({"word": flashcards_json[0]["fields"]["word"], "def": flashcards_json[0]["fields"]["definition"]})