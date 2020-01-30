import Requests
import json
import Token
import pytest


def test_add_benchmark_link_status():
    response = Requests.add_benchmark_link()
    assert response.status_code == 200
    Requests.delete_benchmark_link()


def test_uuid_add_benchmark_link():
    response = Requests.add_benchmark_link()
    a = json.loads(response.text)['data']['addBenchmarkLink']['uuid']
    assert a is not None


def test_location_id_add_benchmark_link():
    response = Requests.add_benchmark_link()
    a = json.loads(response.text)['data']['addBenchmarkLink']['benchmarkLocationId']
    assert a == Requests.benchmarkLocationId


def test_data_add_benchmark_link():
    response = Requests.add_benchmark_link()
    a = json.loads(response.text)['data']['addBenchmarkLink']['data']
    assert a == Requests.data


def test_user_id_add_benchmark_link():
    response = Requests.add_benchmark_link()
    a = json.loads(response.text)['data']['addBenchmarkLink']['createUserId']
    assert a == Token.user_id


def test_read_benchmark_link_status(b):
    a = b
    response = Requests.read_benchmark_link(a)
    assert response.status_code == 200


def test_uuid_read_benchmark_link(f_uuid):
    response = Requests.read_benchmark_link(f_uuid)
    a = json.loads(response.text)['data']['readBenchmarkLink']['uuid']
    assert a == f_uuid


def test_location_id_read_benchmark_link(f_uuid):
    response = Requests.read_benchmark_link(f_uuid)
    a = json.loads(response.text)['data']['readBenchmarkLink']['benchmarkLocationId']
    assert a == Requests.benchmarkLocationId


def test_data_read_benchmark_link(f_uuid):
    response = Requests.read_benchmark_link(f_uuid)
    a = json.loads(response.text)['data']['readBenchmarkLink']['data']
    assert a == Requests.data


def test_user_id_read_benchmark_link(f_uuid):
    response = Requests.read_benchmark_link(f_uuid)
    a = json.loads(response.text)['data']['readBenchmarkLink']['createUserId']
    assert a == Token.user_id


def test_update_benchmark_link_status(b):
    Requests.update_benchmark_link(b)
    assert Requests.update_benchmark_link == 200


def test_uuid_update_benchmark_link(f_uuid):
    response = Requests.update_benchmark_link(f_uuid)
    a = json.loads(response.text)['data']['updateBenchmarkLink']['uuid']
    assert a == f_uuid


def test_location_id_update_benchmark_link(f_uuid):
    response = Requests.update_benchmark_link(f_uuid)
    a = json.loads(response.text)['data']['updateBenchmarkLink']['benchmarkLocationId']
    assert a == Requests.benchmarkLocationId


def test_data_update_benchmark_link(f_uuid):
    response = Requests.update_benchmark_link(f_uuid)
    a = json.loads(response.text)['data']['updateBenchmarkLink']['data']
    assert a == Requests.data_update


def test_user_id_update_benchmark_link(f_uuid):
    response = Requests.update_benchmark_link(f_uuid)
    a = json.loads(response.text)['data']['updateBenchmarkLink']['createUserId']
    assert a == Token.user_id


def test_delete_benchmark_link_status(f_uuid):
    response = Requests.delete_benchmark_link(f_uuid)
    print(response.status_code)
    assert response.status_code == 200


def test_delete_benchmark_link(f_uuid):
    response = Requests.delete_benchmark_link(f_uuid)
    a = json.loads(response.text)['data']['delBenchmarkLink']
    assert a is True


def test_read_benchmark_locations_status():
    response = Requests.read_benchmark_locations(uuid)
    assert response.status_code == 200


# test_add_benchmark_link_status()
uuid = Requests.get_uuid()
print(uuid)
test_read_benchmark_link_status(uuid)
test_update_benchmark_link_status(uuid)
test_read_benchmark_locations_status(uuid)
test_delete_benchmark_link_status(uuid)
uuid = Requests.get_uuid()
print(uuid)
test_delete_benchmark_link(uuid)

