from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.


def receipes(request):
    # Data Insert Start
    if request.method == "POST":
        data = request.POST

        name = data.get("recipe_name")
        desription = data.get("recipe_desription")
        img = request.FILES.get("recipe_img")

        Recipe.objects.create(
            recipe_name=name, recipe_desription=desription, recipe_img=img
        )

        return redirect("/receipe/")

    # Data View Start
    Data = Recipe.objects.all()

    # Data Insert End
    search = request.GET.get("Search")
    if search:
        # print(f"Search : {search}")
        Data = Data.filter(recipe_name__icontains=search)
    # search End

    context = {
        "title": "Receipe App",
        "data": Data,
    }
    return render(request, "receipe.html", context)
    # Data View End


def delete_receipe(request, id):

    # if id == int:
    #     return HttpResponse(f"{id} is NUM")
    # else:
    #     return HttpResponse(f"{id} is Not NUM")

    x = Recipe.objects.get(id=id)

    # print(x.id)
    # print(x.recipe_name)

    # if id == int:
    #     print(f"{id} is NUM")
    # else:
    #     print(f"{id} is Not NUM")

    x.delete()
    return redirect("/receipe/")


def update_receipe(request, id):

    x = Recipe.objects.get(id=id)

    if request.method == "POST":

        data = request.POST

        name = data.get("recipe_name")
        desription = data.get("recipe_desription")
        img = request.FILES.get("recipe_img")

        x.recipe_name = name
        x.recipe_desription = desription

        if img:
            x.recipe_img = img

        x.save()
        return redirect("/receipe/")

    context = {"Update": x, "title": "Update Receipe"}
    return render(request, "update_receipe.html", context)
