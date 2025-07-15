from rest_framework import serializers
from ..models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'book', 'quantity', 'order_date', 'status']
        