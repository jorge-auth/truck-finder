import pytest

@pytest.mark.django_db
def test_fit_cluster0(get_cluster_id_obj, coord0):
    ci = get_cluster_id_obj(coord0[0], coord0[1])
    assert ci == 0

@pytest.mark.django_db
def test_fit_cluster1(get_cluster_id_obj, coord1):
    ci = get_cluster_id_obj(coord1[0], coord1[1])
    assert ci == 1

@pytest.mark.django_db
def test_fit_cluster2(get_cluster_id_obj, coord2):
    ci = get_cluster_id_obj(coord2[0], coord2[1])
    assert ci == 2

@pytest.mark.django_db
def test_fit_cluster3(get_cluster_id_obj, coord3):
    ci = get_cluster_id_obj(coord3[0], coord3[1])
    assert ci == 3

@pytest.mark.django_db
def test_fit_cluster4(get_cluster_id_obj, coord4):
    ci = get_cluster_id_obj(coord4[0], coord4[1])
    assert ci == 4


@pytest.mark.django_db
def test_fit_cluster5(get_cluster_id_obj, coord5):
    ci = get_cluster_id_obj(coord5[0], coord5[1])
    assert ci == 5

@pytest.mark.django_db
def test_fit_cluster6(get_cluster_id_obj, coord6):
    ci = get_cluster_id_obj(coord6[0], coord6[1])
    assert ci == 6

@pytest.mark.django_db
def test_fit_cluster7(get_cluster_id_obj, coord7):
    ci = get_cluster_id_obj(coord7[0], coord7[1])
    assert ci == 7

@pytest.mark.django_db
def test_fit_cluster8(get_cluster_id_obj, coord8):
    ci = get_cluster_id_obj(coord8[0], coord8[1])
    assert ci == 8

@pytest.mark.django_db
def test_fit_cluster9(get_cluster_id_obj, coord9):
    ci = get_cluster_id_obj(coord9[0], coord9[1])
    assert ci == 9