from rest_framework.exceptions import ValidationError

def validate_latitude_longitude(latitude, longitude):
    # Define the valid range for latitude and longitude
    valid_latitude_range = (-90, 90)
    valid_longitude_range = (-180, 180)

    # Check if latitude is within the valid range
    if not valid_latitude_range[0] <= latitude <= valid_latitude_range[1]:
        raise ValidationError("Latitude is out of bounds")

    # Check if longitude is within the valid range
    if not valid_longitude_range[0] <= longitude <= valid_longitude_range[1]:
        raise ValidationError("Longitude is out of bounds")