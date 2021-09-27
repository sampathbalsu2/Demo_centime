import json
import time

import jsonpath
import pytest
import requests

@pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.parametrize("url", ["https://www.alphavantage.co/query"])
def test_validatResponseCode(url):
        print("****************************Test begins****************************")
        p ={"function": "TIME_SERIES_DAILY", "symbol": "IBM", "apikey": "GO6CLEZU3YKXR1KC"}
        start_time = time.time()
        resp = requests.get(url,params=p, timeout=10)
        end_time = time.time()
        time_taken = end_time - start_time
        print("time taken to receive the response is "+str(time_taken))
        print("Api URL is " + resp.url)
        print("Api response is " + json.dumps(resp.json(), indent=4))
        assert resp.status_code == 200
        print("********************************end ofthe test*************************")

@pytest.mark.parametrize("url", ["https://www.alphavantage.co/query"])
def test_ValidateSymbol(url):
    print("****************************Test begins****************************")
    p = {"function": "TIME_SERIES_DAILY", "symbol": "IBM", "apikey": "GO6CLEZU3YKXR1KC"}
    start_time = time.time()
    resp = requests.get(url, params=p, timeout=10)
    end_time = time.time()
    time_taken = end_time - start_time
    print("time taken to receive the response is " + str(time_taken))
    print("Api URL is " + resp.url)
    print("Api response is " + json.dumps(resp.json(), indent=4))
    json_resp = resp.json()
    print(json_resp["Meta Data"]["2. Symbol"])
    assert json_resp["Meta Data"]["2. Symbol"] == "IBM"
    print("******************************** end ofthe test *************************")