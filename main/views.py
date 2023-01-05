from django.shortcuts import render
from django.http import HttpResponse
from .models import List
from datetime import datetime
from django.http import JsonResponse
# Create your views here.


def index(request):
    list = List.objects.all()
    date = datetime.now().strftime("%Y-%m-%d")

    return render(request, 'index.html', {"lists": list, "date": date})

def submitLits(request):
    title = request.POST.get("title")
    list = List(title=title)
    list.save()
    # return render(request, 'index.html', {"id": list.id, "title": list.title})
    data = {"id": list.id, "title": list.title}
    return JsonResponse(data, safe=False)    

def deleteList(request, id):
    List.objects.get(id=id).delete()
    # return render(request, 'index.html')
    return JsonResponse({"ok": True}, safe=False)    

def editList(request, id):
    title = request.POST.get("title")
    edit_list = List.objects.get(id=id)
    edit_list.title = title
    edit_list.save()
    # return render(request, 'index.html', {"title": edit_list.title})
    data = {"title": edit_list.title}
    return JsonResponse(data, safe=False) 