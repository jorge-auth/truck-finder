from private_api.models import (
    Cluster,
    FoodTruck
)
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from joblib import dump, load


def populate_clusters():
    for i in range(11):
        c = Cluster(cluster_id=i)
        c.save()


def preprocessing_and_populate_trucks():
    """
    /!\ Caution clusters will be attributed with different numbers despite the regions 
    are the same. Should only be loaded once. The locationid as an unique element guarantees 
    that.
    """
    #extract data from the csv file
    food_trucks_df = pd.read_csv('dataset/food-truck-data.csv')
    
    coordinates = food_trucks_df[['Latitude', 'Longitude']]

    scaler = StandardScaler()
    coordinates_scaled = scaler.fit_transform(coordinates)
    kmeans = KMeans(n_clusters=10)
    food_trucks_df['cluster'] = kmeans.fit_predict(coordinates_scaled)
    import sys
    print(sys.path)


    dump(kmeans, './src/private_api/kmeans_model/kmeans_model.joblib')
    dump(scaler, './src/private_api/kmeans_model/scaler.joblib')


    #Load the trucks in the database
    for index, row in food_trucks_df.iterrows():
        #get the cluster
        input_coords_scaled = scaler.transform([[
            row["Latitude"], 
            row["Longitude"]]]
        )

        cluster_id = kmeans.predict(input_coords_scaled)[0]
        C_i, created = Cluster.objects.get_or_create(
            cluster_id=cluster_id,
        )

        food_truck_instance = FoodTruck.objects.get_or_create(
            locationid = row["locationid"],
            Applicant = row["Applicant"],
            FacilityType = row["FacilityType"],
            Address = row["Address"],
            Latitude = row["Latitude"],
            Longitude = row["Longitude"],
            cluster=C_i,  # Link to the Cluster instance
        )
        
        print("Food truck loading complete!")

def get_cluster_id(latitude, longitude):
    kmeans_model = load('./src/private_api/kmeans_model/kmeans_model.joblib')
    scaler = load('./src/private_api/kmeans_model/scaler.joblib')
    
    # Standardize the input coordinates using the same 
    input_coords_scaled = scaler.transform([[latitude, longitude]])

    # Predict the cluster for the input coordinates
    cluster_id = kmeans_model.predict(input_coords_scaled)[0]

    return cluster_id

def print_cluster_lat_lon_from_model():

    # Load the KMeans model and scaler
    kmeans_model = load('./src/private_api/kmeans_model/kmeans_model.joblib')
    scaler = load('./src/private_api/kmeans_model/scaler.joblib')

    # Retrieve the cluster centers
    cluster_centers_scaled = kmeans_model.cluster_centers_

    # Inverse transform the scaled cluster centers to obtain original coordinates
    cluster_centers_original = scaler.inverse_transform(cluster_centers_scaled)

    # Print the result
    for cluster_id, (latitude, longitude) in enumerate(cluster_centers_original):
        print(f"Cluster {cluster_id}: Latitude={latitude}, Longitude={longitude}")