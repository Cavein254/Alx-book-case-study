import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from ..models.order import Order, OrderItem

NUM_ORDERS = 1000
MAX_ITEMS_PER_ORDER = 5

class Command(BaseCommand):
    help = 'Seed the database with orders and order items'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding orders database...'))
        fake = Faker()

        self.stdout.write("Deleting existing data...")
        Order.objects.all().delete()
        OrderItem.objects.all().delete()

        customers = list(Order.objects.values_list('customer', flat=True).distinct())
        books = list(OrderItem.objects.values_list('book', flat=True).distinct())

        self.stdout.write(self.style.SUCCESS(f'Creating orders {NUM_ORDERS}...'))
        for _ in range(NUM_ORDERS):
            order = Order.objects.create(
                customer=random.choice(customers),
                total_amount=round(random.uniform(20.0, 500.0), 2),
                status=random.choice(Order.STATUS_CHOICES)[0]
            )
            num_items = random.randint(1, MAX_ITEMS_PER_ORDER)
            for _ in range(num_items):
                book = random.choice(books)
                quantity = random.randint(1, 3)
                price = round(random.uniform(5.0, 100.0), 2)
                OrderItem.objects.create(
                    order=order,
                    book_id=book,
                    quantity=quantity,
                    price=price
                )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {NUM_ORDERS} orders with items.'))