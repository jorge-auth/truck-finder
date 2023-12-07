# private_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from private_api.models import FoodTruck
from private_api.serializers import FoodTruckSerializer
from private_api.helpers import get_cluster_id

from sklearn.neighbors import KDTree


class FoodTruckListView(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieve lat and lon from query parameters, default to None
        lat = request.query_params.get('lat', None)
        lon = request.query_params.get('lon', None)

        # Validate lat and lon, perform necessary checks

        # Assuming you have a method to filter FoodTrucks based on lat and lon
        food_trucks = self.filter_food_trucks(lat, lon)

        coordinates = [(ft.Latitude, ft.Longitude) for ft in food_trucks]
        kdtree = KDTree(coordinates)

        
        # Query the KDTree to find the indices of the 5 nearest neighbors
        _, indices = kdtree.query([[lat, lon]], k=5)
        
        # Convert NumPy array to a list of integers
        food_trucks_list = list(food_trucks)

        # Convert NumPy array to a list of integers
        indices_list = indices.tolist()[0]

        # Retrieve the 5 closest FoodTrucks using a loop
        closest_food_trucks = [food_trucks_list[i] for i in indices_list]


        serializer = FoodTruckSerializer(closest_food_trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def filter_food_trucks(self, lat, lon):
        target_cluster_id = get_cluster_id(lat, lon)
        return FoodTruck.objects.filter(cluster_id=target_cluster_id)  # Placeholder, change it as needed
