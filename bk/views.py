from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
import os,json
from os import listdir
from os.path import isfile, join
from django.core.mail import send_mail


FILEPATH = os.path.dirname(os.path.abspath(__file__))+"/"

# Create your views here.

def notify(update,name):
    c = lambda x: x[0].upper() + x[1:]
    to_email = "kandrosc@ualberta.ca" if name == "baylee" else "baylee1@ualberta.ca"
    send_mail("Baylee and Kyle's Internet Home",c(name)+" has added a new "+update+"!","bksite3@gmail.com",[to_email],fail_silently=False,)


def index(request):
    return render(request,"index.html")

def pictures(request):
    data = request.POST
    files = request.FILES
    pictures = sorted([f.split(".")[0] for f in listdir(FILEPATH+"/static/images/") if isfile(join(FILEPATH+"/static/images/", f))])
    try:
        uploaded_picture = files["picture"].read()
        print(uploaded_picture)
        newnum = str(int(pictures[-1])+1)
        with open(FILEPATH+"/static/images/{}.jpg".format(newnum),"wb") as f: f.write(uploaded_picture)
        pictures.append(newnum)
        notify("picture",data["who"])
    except MultiValueDictKeyError: pass
    path = request.build_absolute_uri().replace("pictures","images")
    
    elms = ""
    for p in pictures:
        elms += '<li><img class="picture" src="{}" width="420" height="315"></li>'.format(path+"/"+p)

    return render(request,"pictures.html",{"pictures":elms})

def songs(request):
    data = request.POST
    with open(FILEPATH+"static/songs.txt","r") as f: songs = f.read().splitlines()
    try:
        songs.append(data["url"].replace("watch?v=","embed/"))
        with open(FILEPATH+"static/songs.txt","w") as f: f.write("\n".join(songs))
        notify("song",data["who"])
    except MultiValueDictKeyError: pass
    elms = ""
    for url in songs:
        elms += '<li><iframe width="420" height="315" src="{}" frameborder="0" gesture="media" allow="autoplay; encrypted-media" allowfullscreen></iframe></li>'.format(url)
    return render(request,"songs.html",{"songs":elms})

def activities(request):
    data = request.POST
    with open(FILEPATH+"static/activities.json","r") as f: act = json.load(f)
    try:
        newindex = str(int(list(act.keys())[-1])+1)
        act[newindex] = {"name":data["who"],"activity":data["activity"]}
        with open(FILEPATH+"static/activities.json","w") as f: json.dump(act,f)
        notify("activity",data["who"])
    except MultiValueDictKeyError: pass
    elms = ""
    for i in act:
        name, activity = act[i]["name"], act[i]["activity"]
        elms += '<li class="{0}">{1}</li>'.format(name,activity)

    return render(request,"activities.html",{"activities":elms})

def things(request):
    data = request.POST
    with open(FILEPATH+"static/things.json","r") as f: things = json.load(f)
    try:
        newindex = str(int(list(things.keys())[-1])+1)
        things[newindex] = {"name":data["who"],"thing":data["thing"]}
        with open(FILEPATH+"static/things.json","w") as f: json.dump(things,f)
        notify("thing they love",data["who"])
    except MultiValueDictKeyError: pass
    elms = ""
    for i in things:
        name, thing = things[i]["name"], things[i]["thing"]
        elms += '<li class="{0}">{1}</li>'.format(name,thing)

    return render(request,"things.html",{"things":elms})

def memories(request):
    data = request.POST
    with open(FILEPATH+"static/memories.json","r") as f: memories = json.load(f)
    try:
        newindex = str(int(list(memories.keys())[-1])+1)
        memories[newindex] = {"name":data["who"],"memory":data["memory"]}
        with open(FILEPATH+"static/memories.json","w") as f: json.dump(memories,f)
        notify("memory",data["who"])
    except MultiValueDictKeyError: pass
    elms = ""
    for i in memories:
        name, memory = memories[i]["name"], memories[i]["memory"]
        elms += '<li class="{0}">{1}</li>'.format(name,memory)

    return render(request,"memories.html",{"memories":elms})






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


def image(request,image_num):
    pictures = [f for f in listdir(FILEPATH+"/static/images/") if isfile(join(FILEPATH+"/static/images/", f))]
    for p in pictures:
        if int(p.split(".")[0]) == image_num:
            picture = p
            break
    with open(FILEPATH+"/static/images/"+picture,"rb") as f: pfile = f.read()
    response = HttpResponse(pfile)
    response["content-type"] = "image/jpeg"
    return response


def css(request):
    with open(FILEPATH+"templates/bk.css","r") as f: css = f.read()
    response = HttpResponse(css)
    response["content-type"] = "text/css"
    return response
