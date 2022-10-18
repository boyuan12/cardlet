from django.shortcuts import render
from newset.models import Set, FlashCard

# Create your views here.
def view_set(request, set_id):
    set = Set.objects.get(set_id=set_id)
    flashcards = FlashCard.objects.filter(set=set)
    return render(request, "viewset/set.html", {
        "set": set,
        "flashcards": flashcards
    })
