from django.contrib import admin
from .models import Product, Order

admin.site.site_header = "E-Commerce Admin Page"
admin.site.site_title = "Tymo's Store"

admin.site.index_title = "Manage"

class ProductAdmin(admin.ModelAdmin):
    # Create a function to change category to default
    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')
        
    # Change action name
    change_category_to_default.short_description = 'Default Category'
    list_display = ['title', 'price', 'discount_price', 'category']
    search_fields = ['title', 'category']
    list_filter = ['category']
    list_editable = ['price', 'discount_price']
    actions = ['change_category_to_default']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)

