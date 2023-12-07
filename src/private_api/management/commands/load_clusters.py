# your_app/management/commands/custom_command.py
from django.core.management.base import BaseCommand
from private_api.helpers import populate_clusters

class Command(BaseCommand):
    help = 'Your custom command description goes here'

    def handle(self, *args, **options):
        # Your command logic goes here
        populate_clusters()
        self.stdout.write(self.style.SUCCESS('Successfully complete load cluster command'))
