# your_app/management/commands/custom_command.py
from django.core.management.base import BaseCommand
from private_api.helpers import preprocessing_and_populate_trucks

class Command(BaseCommand):
    help = 'This changes the kmeans model and populates the foodtruck. do not run unless you are developing a new model solution.'

    def handle(self, *args, **options):
        # Your command logic goes here
        preprocessing_and_populate_trucks()
        self.stdout.write(self.style.SUCCESS('Successfully complete load food trucks command'))
