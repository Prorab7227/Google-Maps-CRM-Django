from django.shortcuts import render
from ..models import Category, Country, City, State, Place

def index(request):
    category_names = Category.objects.all()

    context = {"categories": category_names}
    return render(request, 'index.html', context)

def categoty_list_place(request, category_name):
    category_obj = Category.objects.get(name=category_name)
    places = Place.objects.filter(category=category_obj)

    context = {
        "category_name": category_name,
        "places": places
    }
    return render(request, 'categoty_list_place_def.html', context)

def categoty_list_place_task_manager(request, category_name):
    category_obj = Category.objects.get(name=category_name)
    places = Place.objects.filter(category=category_obj)

    context = {
        "category_name": category_name,
        "places": places
    }
    return render(request, 'categoty_list_place_task_manager.html', context)

def place_full_info(request, name_slug):
    place_obj = Place.objects.get(slug=name_slug)

    context = {"place_obj": place_obj}
    return render(request, 'place_full_info.html', context)