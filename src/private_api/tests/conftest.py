"""
Cluster 0: Latitude=37.80241110316494, Longitude=-122.41259339277755
Cluster 1: Latitude=7.105427357601002e-15, Longitude=0.0
Cluster 2: Latitude=37.74718888247515, Longitude=-122.39304783134442
Cluster 3: Latitude=37.789315814706065, Longitude=-122.40019236610871
Cluster 4: Latitude=37.725249754901505, Longitude=-122.38795321520844
Cluster 5: Latitude=37.77062614623407, Longitude=-122.40266639908815
Cluster 6: Latitude=37.71952167367456, Longitude=-122.4461494198286
Cluster 7: Latitude=37.74992665491735, Longitude=-122.49071288760086
Cluster 8: Latitude=37.77969139100502, Longitude=-122.43060395085435
Cluster 9: Latitude=37.76065070721035, Longitude=-122.41216043239612
"""
import pytest
from private_api.helpers import get_cluster_id

@pytest.fixture
def get_cluster_id_obj():
    yield get_cluster_id 


@pytest.fixture
def coord0():
    lat = 37.80241110316494
    lon = -122.41259339277755
    return (lat, lon)

@pytest.fixture
def coord1():
    lat = 7.105427357601002e-15
    lon = 0.0
    return (lat, lon)

@pytest.fixture
def coord2():
    lat = 37.74718888247515
    lon = -122.39304783134442
    return (lat, lon)

@pytest.fixture
def coord3():
    lat = 37.789315814706065
    lon = -122.40019236610871
    return (lat, lon)

@pytest.fixture
def coord4():
    lat = 37.725249754901505
    lon = -122.38795321520844
    return (lat, lon)

@pytest.fixture
def coord5():
    lat = 37.77062614623407
    lon = -122.40266639908815
    return (lat, lon)

@pytest.fixture
def coord6():
    lat = 37.71952167367456
    lon = -122.4461494198286
    return (lat, lon)

@pytest.fixture
def coord7():
    lat = 37.74992665491735
    lon = -122.49071288760086
    return (lat, lon)

@pytest.fixture
def coord8():
    lat = 37.77969139100502
    lon = -122.43060395085435
    return (lat, lon)

@pytest.fixture
def coord9():
    lat = 37.76065070721035
    lon = -122.41216043239612
    return (lat, lon)