import json
import time

import jsonpath
import pytest
import requests

@pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.parametrize("url", ["https://www.alphavantage.co/query"])
def test_validate_ResponseCode(url):
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

@pytest.mark.skip
@pytest.mark.parametrize("url", ["https://www.alphavantage.co/query"])
def test_Validate_Symbol_present_in_the_repsonse(url):
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

@pytest.mark.skip
@pytest.mark.parametrize("url", ["https://www.alphavantage.co/query"])
def test_apirespone_with_invalidKey(url):
    print("****************************Test begins****************************")
    p = {"function": "TIME_SERIES_DAILY", "symbol": "IBM", "apikey": ""}
    start_time = time.time()
    resp = requests.get(url, params=p, timeout=10)
    end_time = time.time()
    time_taken = end_time - start_time
    print("time taken to receive the response is " + str(time_taken))
    print("Api URL is " + resp.url)
    print("Api response is " + json.dumps(resp.json(), indent=4))
    json_resp = json.loads(resp.text)
    print("Error Message" in json_resp)
    assert "Error Message" in json_resp
    print("******************************** end of the test *************************")

@pytest.mark.skip
@pytest.mark.parametrize("url", ["https://www.alphavantage.co/query"])
def test_check_content_type_equals_json(url):
    p = {"function": "TIME_SERIES_DAILY", "symbol": "IBM", "apikey": "GO6CLEZU3YKXR1KC"}
    start_time = time.time()
    resp = requests.get(url, params=p, timeout=10)
    end_time = time.time()
    time_taken = end_time - start_time
    print("time taken to receive the response is " + str(time_taken))
    print("Api URL is " + resp.url)
    assert resp.headers["Content-Type"] == "application/json", "content type is not application/json"

@pytest.mark.skip
@pytest.mark.parametrize("url", ["https://www.alphavantage.co/query"])
def test_check_content_type_equals_csv(url):
    p = {"function": "TIME_SERIES_DAILY", "symbol": "IBM", "apikey": "GO6CLEZU3YKXR1KC", "datatype":"csv"}
    start_time = time.time()
    resp = requests.get(url, params=p, timeout=10)
    end_time = time.time()
    time_taken = end_time - start_time
    print("time taken to receive the response is " + str(time_taken))
    print("Api URL is " + resp.url)
    print("content type is" +resp.headers["Content-Type"])
    print("Response is " + resp.text)
    assert resp.headers["Content-Type"] == "application/x-download", "content type is not csv"


@pytest.mark.parametrize("url", ["https://www.alphavantage.co/query"])
def test_check_output_contains_100_elements(url):
    p = {"function": "TIME_SERIES_DAILY", "symbol": "IBM", "apikey": "GO6CLEZU3YKXR1KC"}
    start_time = time.time()
    resp = requests.get(url, params=p, timeout=10)
    end_time = time.time()
    time_taken = end_time - start_time
    print("time taken to receive the response is " + str(time_taken))
    print("Api URL is " + resp.url)
    json_resp = resp.json()
    time_series = json_resp["Time Series (Daily)"]
    assert len(time_series.keys()) == 100, "default keys are not 100"