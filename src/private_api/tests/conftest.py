"""
Cluster 1: Latitude=37.77591696106071, Longitude=-122.39756316353638
Cluster 2: Latitude=7.105427357601002e-15, Longitude=0.0
Cluster 3: Latitude=37.74467675458272, Longitude=-122.39364247793189
Cluster 4: Latitude=37.791238783114615, Longitude=-122.40143218491829
Cluster 5: Latitude=37.72497262795293, Longitude=-122.3885875484275
Cluster 6: Latitude=37.765054046592766, Longitude=-122.41975509125709
Cluster 7: Latitude=37.779184251736304, Longitude=-122.42766432637215
Cluster 8: Latitude=37.75719129289442, Longitude=-122.39208176059284
Cluster 9: Latitude=37.71913561680847, Longitude=-122.4543245119097
Cluster 10: Latitude=37.752150988160466, Longitude=-122.48698213502519
"""
import pytest
from private_api.helpers import get_cluster_id

@pytest.fixture
def get_cluster_id_obj():
    yield get_cluster_id 


@pytest.fixture
def coord0():
    lat = 37.77591696106071
    lon=-122.39756316353638
    return (lat, lon)

@pytest.fixture
def coord1():
    lat = 7.105427357601002e-15
    lon = 0.0
    return (lat, lon)

@pytest.fixture
def coord2():
    lat = 37.74467675458272
    lon = -122.39364247793189
    return (lat, lon)

@pytest.fixture
def coord3():
    lat = 37.791238783114615
    lon = -122.40143218491829
    return (lat, lon)

@pytest.fixture
def coord4():
    lat = 37.72497262795293
    lon = -122.3885875484275
    return (lat, lon)

@pytest.fixture
def coord5():
    lat = 37.765054046592766
    lon = -122.41975509125709
    return (lat, lon)

@pytest.fixture
def coord6():
    lat = 37.779184251736304
    lon = -122.42766432637215
    return (lat, lon)

@pytest.fixture
def coord7():
    lat = 37.75719129289442
    lon = -122.39208176059284
    return (lat, lon)

@pytest.fixture
def coord8():
    lat = 37.71913561680847
    lon = -122.4543245119097
    return (lat, lon)

@pytest.fixture
def coord9():
    lat = 37.752150988160466
    lon = -122.48698213502519
    return (lat, lon)