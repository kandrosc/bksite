from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
import os,json

FILEPATH = os.path.dirname(os.path.abspath(__file__))+"/"

# Create your views here.

def index(request):
    return render(request,"index.html")

def pictures(request):
    return render(request,"pictures.html")

def songs(request):
    data = request.POST
    with open(FILEPATH+"static/songs.txt","r") as f: songs = f.read().splitlines()
    try:
        songs.append(data["url"].replace("watch?v=","embed/"))
        with open(FILEPATH+"static/songs.txt","w") as f: f.write("\n".join(songs))
    except MultiValueDictKeyError: pass
    elms = ""
    for url in songs:
        elms += '<li><iframe width="420" height="315" src="{}"></iframe></li>'.format(url)
    return render(request,"songs.html",{"songs":elms})

def activities(request):
    data = request.POST
    with open(FILEPATH+"static/activities.json","r") as f: act = json.load(f)
    try:
        newindex = str(int(list(act.keys())[-1])+1)
        act[newindex] = {"name":data["who"],"activity":data["activity"]}
        with open(FILEPATH+"static/activities.json","w") as f: json.dump(act,f)
    except MultiValueDictKeyError: pass
    elms = ""
    for i in act:
        name, activity = act[i]["name"], act[i]["activity"]
        elms += '<li class="{0}">{1}</li>'.format(name,activity)

    return render(request,"activities.html",{"activities":elms})

def things(request):
    return render(request,"things.html")

def memories(request):
    return render(request,"memories.html")






def pictures_upload(request):
    return render(request,"pictures_upload.html")

def songs_upload(request):
    return render(request,"songs_upload.html")

def activities_upload(request):
    return render(request,"activities_upload.html")

def things_upload(request):
    return render(request,"things_upload.html")

def memories_upload(request):
    return render(request,"memories_upload.html")



def css(request):
    with open(FILEPATH+"templates/bk.css","r") as f: css = f.read()
    response = HttpResponse(css)
    response["content-type"] = "text/css"
    return response
