from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'private_api'


    """    
    def ready(self) -> None:
        from private_api.helpers import (
            populate_clusters,
            preprocessing_and_populate_trucks,
        )

        populate_clusters()
        preprocessing_and_populate_trucks()
    """
    