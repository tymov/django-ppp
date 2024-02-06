from django.shortcuts import redirect, render
from .models import Food, Consume

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        food_consumed = request.POST.get('food_consumed')
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        food_list = Food.objects.all()
        
    else:
        food_list = Food.objects.all()
    
    consumed_foods = Consume.objects.filter(user=request.user)
    return render(request, 'calorietracker/index.html', {'food_list': food_list, 'consumed_foods': consumed_foods})

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'calorietracker/delete.html')