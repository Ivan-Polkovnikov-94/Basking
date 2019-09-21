import requests
import json

origin = 'https://dev-api.basking.io'
staging = 'https://qi2vju2jn9.execute-api.eu-central-1.amazonaws.com/staging'
jwt = 'eyJraWQiOiJKbFZ3SDBmRVdOMmtsOGswN2pHa3N6QWVLQVhzN1FQejBUNThFa3ZVYlA4PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjM2EzODhmYi1kYjFhLTQwOWItODA2NS1kZTg0NzQ4MmQ0MzIiLCJhdWQiOiI3bzV2cXY3dWt0OW9ub2xxMW52anQ3bTQwZSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJldmVudF9pZCI6IjU3MGZjNzEwLTJlZmEtNGZmYS1hMjgyLTg1NjEwNTEyOGJiMCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNTY4OTMyNDcxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtY2VudHJhbC0xLmFtYXpvbmF3cy5jb21cL2V1LWNlbnRyYWwtMV9mYk5SN3A5ZVkiLCJuYW1lIjoiSXZhbiBQb2xrb3ZuaWtvdiIsImNvZ25pdG86dXNlcm5hbWUiOiJjM2EzODhmYi1kYjFhLTQwOWItODA2NS1kZTg0NzQ4MmQ0MzIiLCJleHAiOjE1Njg5NTI3MzEsImlhdCI6MTU2ODk0OTEzMSwiZW1haWwiOiJpdmFuLnBvbGtvdm5pa292Ljk0QGdtYWlsLmNvbSJ9.RHPmes3yIr8YwkSi_93bP1WoLkjWEw8JTj-QNLBmO_nhlcxnz89u3Jh_SO4WyciXlChmMoKcMyFQjE0wAbE_kOMLa7Yd7FsOk3AbrVsrivbCejLiBDZIUVYis6etKItUsg7FQs4AgOVEI2zlucAHeNuHWgMWdCA90_zfq3AFsM7yww5j4jchHWyl0BUb5v94We9sBT6Zo3SKBT9KRyFOrNEkCrliYDqIW053LckqXmo9v2gjTIpA5JqIONaiHXaEudroo2zihzRFuaXIIoM3hcDrNxbWLRztt_QkErn-5gyOD1eYI1dIG7A5CWO2I7oCzEGBGoVGsKTONEbE35fi7Q'


def add_benchmark_link():
    payload = {
        "query": "mutation addBenchmarkLink($input: BenchmarkLinkInput!) {addBenchmarkLink(input: $input) {uuid, "
                 "benchmarkLocationId, data, createUserId}}",
        "variables": {
            "input": {
                "benchmarkLocationId": 1,
                "data": "test",
                "staging": staging,
            }
        }
    }

    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    print(r.text)


def get_uuid(self):
    add_benchmark_link()
    uuid = json.loads(r.text)['data']['addBenchmarkLink']['uuid']
    return uuid


def read_benchmark_link(self, uuid):
    payload = {
        "query": "query getBenchmarkLink($uuid: String) {link: getBenchmarkLink(uuid: $uuid){uuid, "
                 "benchmarkLocationId, data, createUserId}}",
        "variables": {
            "uuid": uuid
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    print(r.text)


def update_benchmark_link(self, uuid):
    payload = {
        "query": "mutation updateBenchmarkLink($uuid: String!, $input: BenchmarkLinkInput!) {link: "
                 "updateBenchmarkLink(uuid: $uuid, input: $input){uuid, benchmarkLocationId, data, createUserId}}",
        "variables": {
            "uuid": uuid,
            "input": {
                "benchmarkLocationId": 1,
                "data": "hello world!"
            }
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    print(r.text)


def delete_benchmark_link(self, uuid):
    payload = {
        "query": "query delBenchmarkLink($uuid: String) {delBenchmarkLink(uuid: $uuid)}",
        "variables": {
            "uuid": uuid
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    print(r.text)


def read_benchmark_locations(self, uuid):
    payload = {
        "query": "query getBenchmarkLocations($organizationId: Int) {locations: getBenchmarkLocations(organizationId: "
                 "$organizationId){id, name, description, rent_prime_per_month, rent_prime_per_year, fit_out_cost, "
                 "density, currency, area_unit}}",
        "variables": {
            "organizationId": 3
        }
    }
    r = requests.post(origin, headers={'Authorization': jwt}, json=payload)
    print(r.text)
