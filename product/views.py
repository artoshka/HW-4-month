from django.shortcuts import render
from .models import Foods, Categories


# Create your views here.

def homepage(request):
    products = Foods.objects.all()  # list
    context = {"all_food": products}
    return render(request, "product_list.html", context)


def Category(request):
    categories = Categories.objects.all()
    context = {"categories": categories}
    return render(request, "categories.html", context)


def categories_info(request, id):
    category = Categories.objects.get(id=id)
    context = {"category": category}
    return render(request, "category_info.html", context)


def Buy(request):
    return render(request, "index.html")

