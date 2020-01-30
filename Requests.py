import requests
import json
import Token

origin = 'https://dev-api.basking.io'
staging = 'https://qi2vju2jn9.execute-api.eu-central-1.amazonaws.com/staging'
jwt = Token.get_token()

data = 'data'
data_update = 'data1'
benchmarkLocationId = 2


def get_uuid():
    payload = {
        "query": "mutation addBenchmarkLink($input: BenchmarkLinkInput!) {addBenchmarkLink(input: $input) {uuid, "
                 "benchmarkLocationId, data, createUserId}}",
        "variables": {
            "input": {
                "benchmarkLocationId": benchmarkLocationId,
                "data": data,
                "staging": staging,
            }
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    a = json.loads(r.text)['data']['addBenchmarkLink']['uuid']
    return a


def add_benchmark_link():
    payload = {
        "query": "mutation addBenchmarkLink($input: BenchmarkLinkInput!) {addBenchmarkLink(input: $input) {uuid, "
                 "benchmarkLocationId, data, createUserId}}",
        "variables": {
            "input": {
                "benchmarkLocationId": benchmarkLocationId,
                "data": data,
                "staging": staging,
            }
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    return r


def read_benchmark_link(uuid):
    payload = {
        "query": "query getBenchmarkLink($uuid: String) {link: getBenchmarkLink(uuid: $uuid){uuid, "
                 "benchmarkLocationId, data, createUserId}}",
        "variables": {
            "uuid": uuid
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    return r


def update_benchmark_link(uuid):
    payload = {
        "query": "mutation updateBenchmarkLink($uuid: String!, $input: BenchmarkLinkInput!) {link: "
                 "updateBenchmarkLink(uuid: $uuid, input: $input){uuid, benchmarkLocationId, data, createUserId}}",
        "variables": {
            "uuid": uuid,
            "input": {
                "benchmarkLocationId": benchmarkLocationId,
                "data": data_update
            }
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    return r


def delete_benchmark_link(uuid):
    payload = {
        "query": "query delBenchmarkLink($uuid: String) {delBenchmarkLink(uuid: $uuid)}",
        "variables": {
            "uuid": uuid
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    return r


def read_benchmark_locations(uuid):
    payload = {
        "query": "query getBenchmarkLocations($organizationId: Int) {locations: getBenchmarkLocations(organizationId: "
                 "$organizationId){id, name, description, rent_prime_per_month, rent_prime_per_year, fit_out_cost, "
                 "density, currency, area_unit}}",
        "variables": {
            "organizationId": 3
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    return r

