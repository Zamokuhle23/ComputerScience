from django.contrib import admin

from customers.models import Customer
from store.models import Product, Comment
from users.models import Seller, Producer, DeliverMan, Shipper




@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("image", "email")
    list_filter = ("email",)


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ("image", "email")
    list_filter = ("email",)


@admin.register(DeliverMan)
class DelivermanAdmin(admin.ModelAdmin):
    list_display = ("image", "email")
    list_filter = ("email",)


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    list_display = ("image", "email")
    list_filter = ("email",)



