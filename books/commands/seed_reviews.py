import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from ..models.reviews import Review
from ..models.book import Book
from ..models.customer import Customer

NUM_REVIEWS = 2500

class Command(BaseCommand):
    help = 'Seed the database with reviews for books'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding reviews database...'))
        fake = Faker()

        self.stdout.write("Deleting existing data...")
        

        books = list(Book.objects.values_list('id', flat=True))
        customers = list(Customer.objects.values_list('id', flat=True))

        

        if not books or not customers:
            self.stdout.write(self.style.ERROR('No books or customers found. Please seed books and customers first.'))
            return
        
        Review.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f'Creating reviews {NUM_REVIEWS}...'))
        for _ in range(NUM_REVIEWS):
            book = random.choice(books)
            reviewer = random.choice(customers)

            if Review.objects.filter(book_id=book, reviewer_id=reviewer).exists():
                continue

            Review.objects.create(
                book_id=book,
                reviewer_id=reviewer,
                rating=random.randint(1, 5),
                comment=fake.paragraph(nb_sentences=random.randint(2, 5)),
                created_at=fake.date_time_between_dates(start_date='-3y', end_date='now')
            )
            
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {NUM_REVIEWS} reviews.'))