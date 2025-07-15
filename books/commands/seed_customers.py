import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker


from ..models.customer import Customer, LoyaltyProgram

NUM_CUSTOMERS = 1000

class Command(BaseCommand):
    help = 'Seed the database with customers and loyalty programs'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding customers database...'))
        fake = Faker()

        self.stdout.write("Deleting existing data...")
        Customer.objects.all().delete()
        
        tier_choices = [choice[0] for choice in LoyaltyProgram.TIER_CHOICES]
        customers = []
        for _ in range(NUM_CUSTOMERS):
            customer = Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address()
            )
            customers.append(customer)
        
        for customer in customers:
            LoyaltyProgram.objects.create(
                customer=customer,
                tier=random.choice(tier_choices),
                points=random.randint(0, 1000)
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {NUM_CUSTOMERS} customers and their loyalty programs.'))

        