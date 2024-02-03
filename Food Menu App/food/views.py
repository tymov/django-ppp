from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import ItemForm
from .models import Item


# Create your views here.

# Hello world view
def index(request):
    return HttpResponse("Hello, world. You're at the food index.")

def item(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'food/items.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context  = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('food:item')
    return render(request, 'food/item-form.html', {'form': form})

def edit_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:item')
    return render(request, 'food/item-form.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:item')
    return render(request, 'food/item-delete.html', {'item': item})