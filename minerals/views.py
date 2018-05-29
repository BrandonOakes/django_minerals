from django.shortcuts import render, get_object_or_404

from .models import Mineral

# Create your views here.


def mineral_list(request):
    """renders template to list html from browser response"""
    minerals = Mineral.objects.all()
    return render(request, 'minerals/list.html', {'minerals':minerals})

def mineral_detail(request, pk):
    """renders template to list html from browser response"""
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html', {'mineral':mineral})
