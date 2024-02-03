from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    # /food/item
    path('item/', views.item, name='item'),
    # /food/item/<item_id>
    path('item/<int:item_id>/', views.detail, name='details'),
    # adding items
    path('item/add/', views.create_item, name='create_item'),
    # editing items
    path('item/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    # deleting items
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
