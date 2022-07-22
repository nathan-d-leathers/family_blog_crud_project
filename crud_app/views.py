import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Author, Entry
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'crud_app/index.html')


def list_authors(request):
    authors = Author.objects.all()
    data = {"authors": authors}
    return render(request, 'crud_app/list_authors.html', data)


def list_entries(request, author_id):
    author_entries = Entry.objects.all().filter(author_id=author_id)
    author_name = Author.objects.all().get(id=author_id)
    data = {"entries": author_entries, "author": author_name}
    return render(request, 'crud_app/list_entries.html', data)


def entry_info(request, author_id, entry_id):
    entry = Entry.objects.all().get(id=entry_id)
    data = {"entry": entry}
    return render(request, 'crud_app/single_entry.html', data)


@csrf_exempt
def add_entry(request, author_id):
    if request.method == "POST":
        body = json.loads(request.body)
        # making the entry object
        newEntry = Entry(
            title=body["title"], description=body["description"], author_id=author_id)
        newEntry.save()
        # if error is found by nto having a response you can add the following code bellow either blank or with data
        # return JsonResponse({}) o return JsonResponse({"sucess":"sucess"})
    return render(request, "crud_app/add_entry.html")
