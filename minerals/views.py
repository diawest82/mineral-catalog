from django.shortcuts import render, get_object_or_404

from .models import Mineral

import random

# Create your views here.


def mineral_list(request):
    '''
    Get all the minerals from the database inside a list
    '''
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'minerals/mineral_list.html', {
        'minerals': minerals, 'random_mineral': random_mineral})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'minerals/mineral_detail.html', {
        'mineral': mineral, 'random_mineral': random_mineral})
