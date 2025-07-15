from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Run all seed commands to populate the database'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))
        
        call_command('seed_base')
        call_command('seed_customers')
        call_command('seed_books')
        call_command('seed_orders')
        call_command('seed_reviews')

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with all data.'))