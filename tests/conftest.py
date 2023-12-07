import pytest
from django.core.management import call_command


@pytest.fixture(autouse=True)
def load_data_from_api_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'clusters_fixture.json')
        call_command('loaddata', 'foodtruck_fixture.json')