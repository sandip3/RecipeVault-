from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='/login/')
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


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
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


def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        p_word = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username !")
            return redirect("/login/")

        user = authenticate(username=username, password=p_word)

        if user is None:
            messages.info(request, "Invalid Password !")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/receipe/")

    context = {
        "title": "Login Account",
    }

    return render(request, "login.html", context)


def logout_page(request):
    logout(request)
    return redirect("/login/")


def register_page(request):

    if request.method == "POST":
        f_name = request.POST.get("first_name")
        l_name = request.POST.get("last_name")
        username = request.POST.get("username")
        p_word = request.POST.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already registered")
            return redirect("/register/")

        user = User.objects.create(
            first_name=f_name,
            last_name=l_name,
            username=username,
            # password = p_word
        )

        user.set_password(p_word)
        user.save()

        messages.success(request, "Account created successfully")
        return redirect("/register/")

    context = {"title": "Register Account"}

    return render(request, "register.html", context)
