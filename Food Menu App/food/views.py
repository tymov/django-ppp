from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

# Hello world view
def index(request):
    return HttpResponse("Hello, world. You're at the food index.")

# Using function based views
def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context  = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)

# Using function based views
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

# Using class based views
class IndexClassView(ListView):
    model = Item;
    template_name = 'food/items.html'
    context_object_name = 'items'    

class FoodDetail(DetailView):
    model = Item;
    template_name = 'food/detail.html'

class CreateFoodItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)