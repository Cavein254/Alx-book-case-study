from rest_framework import viewsets
from models.book import Book
from models.customer import Customer
from models.order import Order
from models.reviews import Review
from serializers.reviewserializer import ReviewSerializer
from serializers.orderserializer import OrderSerializer
from serializers.customerserializer import CustomerSerializer
from serializers.bookserializer import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer