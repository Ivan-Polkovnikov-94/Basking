from baskingRequests import benchmarkRequests
import json
from helpers import token
import pytest
from baskingRequests.benchmarkRequests import update_benchmark_link, read_benchmark_link, add_benchmark_link, \
    benchmarkLocationId, delete_benchmark_link, data, data_update


@pytest.fixture()
def get_uuid():
    response, building = add_benchmark_link()
    return building


def destroy_uuid(building):
    delete_benchmark_link(building)
    building.addfinalizer(destroy_uuid)


class TestAddBenchmarkLink:

    def test_status_code_add_benchmark_link(self):
        response, building = add_benchmark_link()
        assert response.status_code == 200

    def test_uuid_add_benchmark_link(self):
        response, building = add_benchmark_link()
        assert building is not None

    def test_location_id_add_benchmark_link(self):
        response, building = add_benchmark_link()
        a = json.loads(response.text)['data']['addBenchmarkLink']['benchmarkLocationId']
        assert a == benchmarkLocationId

    def test_data_add_benchmark_link(self):
        response, building = add_benchmark_link()
        a = json.loads(response.text)['data']['addBenchmarkLink']['data']
        assert a == benchmarkRequests.data

    def test_user_id_add_benchmark_link(self):
        response, building = add_benchmark_link()
        a = json.loads(response.text)['data']['addBenchmarkLink']['createUserId']
        assert a == token.user_id


class TestReadBenchmarkLink:

    def test_status_code_read_benchmark_link(self, get_uuid):
        response = read_benchmark_link(get_uuid)
        assert response.status_code == 200

    def test_uuid_read_benchmark_link(self, get_uuid):
        response = read_benchmark_link(get_uuid)
        a = json.loads(response.text)['data']['readBenchmarkLink']['uuid']
        assert a == get_uuid

    def test_location_id_read_benchmark_link(self, get_uuid):
        response = read_benchmark_link(get_uuid)
        a = json.loads(response.text)['data']['readBenchmarkLink']['benchmarkLocationId']
        assert a == benchmarkLocationId

    def test_data_read_benchmark_link(self, get_uuid):
        response = read_benchmark_link(get_uuid)
        a = json.loads(response.text)['data']['readBenchmarkLink']['data']
        assert a == data

    def test_user_id_read_benchmark_link(self, get_uuid):
        response = read_benchmark_link(get_uuid)
        a = json.loads(response.text)['data']['readBenchmarkLink']['createUserId']
        assert a == token.user_id


class TestUpdateBenchmarkLink:

    def test_update_benchmark_link_status(self, get_uuid):
        update_benchmark_link(get_uuid)
        assert update_benchmark_link == 200

    def test_uuid_update_benchmark_link(self, get_uuid):
        response = update_benchmark_link(get_uuid)
        a = json.loads(response.text)['data']['updateBenchmarkLink']['uuid']
        assert a == self

    def test_location_id_update_benchmark_link(self, get_uuid):
        response = update_benchmark_link(get_uuid)
        a = json.loads(response.text)['data']['updateBenchmarkLink']['benchmarkLocationId']
        assert a == benchmarkLocationId

    def test_data_update_benchmark_link(self, get_uuid):
        response = update_benchmark_link(get_uuid)
        a = json.loads(response.text)['data']['updateBenchmarkLink']['data']
        assert a == data_update

    def test_user_id_update_benchmark_link(self, get_uuid):
        response = update_benchmark_link(get_uuid)
        a = json.loads(response.text)['data']['updateBenchmarkLink']['createUserId']
        assert a == token.user_id


class TestDeleteBenchmark:

    def test_delete_benchmark_link_status(self, get_uuid):
        response = delete_benchmark_link(get_uuid)
        print(response.status_code)
        assert response.status_code == 200

    def test_delete_benchmark_link(self, get_uuid):
        response = delete_benchmark_link(get_uuid)
        a = json.loads(response.text)['data']['delBenchmarkLink']
        assert a is True
