import Requests
import pytest


class TestBenchmark:

    def test_add_benchmark_link(self):
        Requests.add_benchmark_link
        assert Requests.add_benchmark_link.status_code == 200

    def test_read_benchmark_link(self):
        Requests.read_benchmark_link(Requests.get_uuid)
        assert Requests.read_benchmark_link.status_code == 200

    def test_update_benchmark_link(self):
        Requests.update_benchmark_link(Requests.get_uuid)
        assert Requests.update_benchmark_link.status_code == 200

    def test_delete_benchmark_link(self):
        Requests.delete_benchmark_link(Requests.get_uuid)
        assert Requests.delete_benchmark_link.status_code == 200

    def test_read_benchmark_locations(self):
        Requests.read_benchmark_locations(Requests.get_uuid)
        assert Requests.read_benchmark_locations.status_code == 200
