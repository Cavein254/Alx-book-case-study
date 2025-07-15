import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from ..models.book import Book, Author, Genre, Publisher

NUM_AUTHORS = 300
NUM_PUBLISHERS = 60
NUM_BOOKS = 1000


GENRE_LIST = [
    "Science Fiction", "Fantasy", "Mystery", "Thriller", "Romance", "Horror",
    "Historical Fiction", "Non-Fiction", "Biography", "Poetry", "Humor",
    "Adventure", "Dystopian", "Young Adult", "Children's", "Crime", "Drama"
]
LANGUAGE_LIST = ["English", "Spanish", "French", "German", "Japanese"]

class Command(BaseCommand):
    help = 'Seed the database with books, authors, genres, and publishers'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding books database...'))
        fake = Faker()

        self.stdout.write("Deleting existing data...")
        Book.objects.all().delete()
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Genre.objects.all().delete()

        genres = [Genre.objects.create(name=genre) for genre in GENRE_LIST]
        Publishers = [Publisher.objects.create(
            name=fake.company(),
            address=fake.address()
        ) for _ in range(NUM_PUBLISHERS)]
        authors = [Author.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        ) for _ in range(NUM_AUTHORS)]

        self.stdout.write(self.style.SUCCESS(f'Creating books {NUM_BOOKS}...'))
        format_choices = [choice[0] for choice in Book.FORMAT_CHOICES]
        for _ in range(NUM_BOOKS):
            book = Book.objects.create(
                title=" ".join(fake.words(nb=random.randint(2, 5))).title(),
                publisher=random.choice(Publishers),
                language=random.choice(LANGUAGE_LIST),
                price=round(random.uniform(5.0, 100.0), 2),
                publication_date=fake.date_between(start_date='-30y', end_date='today'),
                format=random.choice(format_choices)
            )   
            book.authors.set(random.sample(authors, k=random.randint(1, 3)))
            book.genres.set(random.sample(genres, k=random.randint(1, 3)))
            book.save()
            
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {NUM_BOOKS} books.'))