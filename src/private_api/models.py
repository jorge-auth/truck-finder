"""
Index(['locationid', 'Applicant', 'FacilityType', 'cnn', 'LocationDescription',
       'Address', 'blocklot', 'block', 'lot', 'permit', 'Status', 'FoodItems',
       'X', 'Y', 'Latitude', 'Longitude', 'Schedule', 'dayshours', 'NOISent',
       'Approved', 'Received', 'PriorPermit', 'ExpirationDate', 'Location',
       'Fire Prevention Districts', 'Police Districts', 'Supervisor Districts',
       'Zip Codes', 'Neighborhoods (old)'],
      dtype='object')

      /!\ I ignored the fields that arent camelcase. Since it is for demo purposes
      most of the data included in the model doesnt change the purpose of the challenge.
"""

from django.db import models

class Cluster(models.Model):
    cluster_id = models.AutoField(primary_key=True)

class FoodTruck(models.Model):
    id = models.AutoField(primary_key=True)
    locationid = models.IntegerField(blank=True, null=True)
    Applicant = models.CharField(max_length=255,null=True, blank=True)
    FacilityType = models.CharField(max_length=255, null=True, blank=True)
    Address = models.CharField(max_length=255, null=True, blank=True)
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    