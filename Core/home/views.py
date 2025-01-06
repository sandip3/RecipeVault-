from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    peoples = [
        {"name": "Sandip", "age": 18},
        {"name": "Pradip", "age": 23},
        {"name": "Ayan", },
        {"name": "Lucky", "age": 15},
        {"name": "Parth", "age": 22},
        {"name": "Harsh", "age": 24},
        {"name": "Aman", "age": 26},
        {"name": "Mosambi", "age": 27},
    ]

    text = """Lorem ipsum dolor, sit amet consectetur adipisicing elit. A corrupti officiis quod voluptas eligendi laborum voluptatem fugit quaerat tenetur. Consequatur alias officia optio? Quae exercitationem quibusdam quos iste aliquam optio?Lorem ipsum dolor, sit amet consectetur adipisicing elit. A corrupti officiis quod voluptas eligendi laborum voluptatem fugit quaerat tenetur. Consequatur alias officia optio? Quae exercitationem quibusdam quos iste aliquam optio?Lorem ipsum dolor, sit amet consectetur adipisicing elit. A corrupti officiis quod voluptas eligendi laborum voluptatem fugit quaerat tenetur. Consequatur alias officia optio? Quae exercitationem quibusdam quos iste aliquam optio?Lorem ipsum dolor, sit amet consectetur adipisicing elit. A corrupti officiis quod voluptas eligendi laborum voluptatem fugit quaerat tenetur. Consequatur alias officia optio? Quae exercitationem quibusdam quos iste aliquam optio?"""

    fruite = ["Apple", "Bannana", "Carry"]

    context = {"person": peoples, "txt": text, "Yam": fruite, "title": "Home Page"}
    return render(request, "home/index.html", context)
    # return HttpResponse("Hello")


def about(request):
    context = {"title": "About Page"}
    return render(request, "home/about.html", context)


def contect(request):
    context = {"title": "Contect Page"}
    return render(request, "home/contect.html", context)
