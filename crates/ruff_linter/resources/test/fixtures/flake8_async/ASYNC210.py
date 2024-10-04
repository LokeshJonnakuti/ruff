import urllib
import requests
import httpx
import urllib3


async def foo():
    urllib.request.urlopen("http://example.com/foo/bar").read()  # ASYNC210


async def foo():
    requests.get(timeout=60)  # ASYNC210


async def foo():
    httpx.get()  # ASYNC210


async def foo():
    requests.post(timeout=60)  # ASYNC210


async def foo():
    httpx.post()  # ASYNC210


async def foo():
    requests.get(timeout=60)  # ASYNC210
    requests.get(..., timeout=60)  # ASYNC210
    requests.get  # Ok
    print(requests.get(timeout=60))  # ASYNC210
    print(requests.get(requests.get(timeout=60), timeout=60))  # ASYNC210

    requests.options(timeout=60)  # ASYNC210
    requests.head(timeout=60)  # ASYNC210
    requests.post(timeout=60)  # ASYNC210
    requests.put(timeout=60)  # ASYNC210
    requests.patch(timeout=60)  # ASYNC210
    requests.delete(timeout=60)  # ASYNC210
    requests.foo()

    httpx.options("")  # ASYNC210
    httpx.head("")  # ASYNC210
    httpx.post("")  # ASYNC210
    httpx.put("")  # ASYNC210
    httpx.patch("")  # ASYNC210
    httpx.delete("")  # ASYNC210
    httpx.foo()  # Ok

    urllib3.request()  # ASYNC210
    urllib3.request(...)  # ASYNC210

    urllib.request.urlopen("")  # ASYNC210

    r = {}
    r.get("not a sync http client")  # Ok


async def bar():

    def request():
        pass

    request()  # Ok

    def urlopen():
        pass

    urlopen()  # Ok
