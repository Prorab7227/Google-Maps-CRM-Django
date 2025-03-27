from django.shortcuts import render
from ..models import Category, Country, City, State, Place

def index(request):
    category_names = Category.objects.all()

    for category in category_names:
        category.save()

    context = {"categories": category_names}
    return render(request, 'index.html', context)

from django.core.paginator import Paginator
from django.http import JsonResponse
def categoty_list_place_tm(request):
    category_name = request.GET.get("category_name")
    page_number = request.GET.get("page", 1)
    items_per_page = 50

    if category_name:
        category_obj = Category.objects.get(slug=category_name)
        places = Place.objects.filter(category=category_obj).order_by("category")
    else:
        places = Place.objects.all().order_by("category")

    paginator = Paginator(places, items_per_page)
    page_obj = paginator.get_page(page_number)

    context = {
        "category_name": category_name,
        "places": page_obj
    }
    return render(request, 'categoty_list_place_tm.html', context)

def place_full_info(request, name_slug):
    place_obj = Place.objects.get(slug=name_slug)

    context = {"place_obj": place_obj}
    return render(request, 'place_full_info.html', context)