from django.contrib import admin
from .models import Product, Comment
from .models import Category
from .models import Customer
from .models import Order

class AdminProduct(admin.ModelAdmin):
	list_display = ['id', 'name','price','category', 'date']


class AdminCategory(admin.ModelAdmin):
	list_display = ['name']



@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
	list_display = ['id','phone','email']
	list_filter = ("id",)


admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
# admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Comment)
