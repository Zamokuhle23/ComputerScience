from rest_framework import serializers

from customers.models import Customer
from store.models import Category, Order, Product
from store.models.Comment import Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name"]





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields  = ["id","name","price","category","description","image","date"]

class CommentSerializer(serializers.ModelSerializer):
    product_connected = ProductSerializer(many=False)
    class Meta:
        model = Comment
        fields  = ["id","author","date_posted","product_connected","content"]

class EagerLoadingMixin:
    @classmethod
    def setup_eager_loading(cls, queryset):
        """
        This function allow dynamic addition of the related objects to
        the provided query.
        @parameter param1: queryset
        """

        if hasattr(cls, "select_related_fields"):
            queryset = queryset.select_related(*cls.select_related_fields)
        if hasattr(cls, "prefetch_related_fields"):
            queryset = queryset.prefetch_related(*cls.prefetch_related_fields)
        return queryset

class OrderSerializer(serializers.ModelSerializer,EagerLoadingMixin):
    product = ProductSerializer(many=False)
    select_related_fields = ('product',)
    prefetch_related_fields = ()

    class Meta:
        model = Order
        fields = ["id", "product", "customer", "quantity", "price", "date", "address", "phone", "completed"]




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields  = ["id","customer","image","email","phone"]