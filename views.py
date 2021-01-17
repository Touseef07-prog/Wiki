from django.shortcuts import render

import random
from . import util
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_entry(request,name):
    return render(request, "encyclopedia/entry.html", {
    "show_entry":util.get_entry(name), "name":name

    })

def search(request):
    found=[]
    if request.method == "POST":
        search_entry=request.POST.get('labb')
        get = util.list_entries()
        for i in get:
            if search_entry in i:
                found.append(i)

                return render(request, "encyclopedia/search.html", {
                "found_entry":found})
                break
        else:
            return HttpResponse("error")


def new_page(request):
        return render(request, "encyclopedia/page.html")

def create_page(request):
    if request.method == "POST":
        title=request.POST.get('title')
        cont=request.POST.get('cont')
        d=util.list_entries()
        for i in d:
            if title == i:
                return HttpResponse("Already exist")
                break
        util.save_entry(title,cont)
        return render(request,"encyclopedia/index.html",{
        "entry":util.list_entries()
        })

def edit(request,name):
    name_content=util.get_entry(name)
    return render(request,"encyclopedia/edit.html",{"content":name_content})

def editing(request):
    if request.method == "POST":
        editable=request.POST.get('text_edit')
        nam=request.POST.get('Change_title')
        util.save_entry(nam,editable)
        return HttpResponse("Edited")

def Random(request):
    return render(request,"encyclopedia/random.html",{
    "entries":random.choice(util.list_entries())
    })
