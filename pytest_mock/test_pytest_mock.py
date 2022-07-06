from pathlib import Path

import requests
from pytest import MonkeyPatch

import functions_mock
from functions_mock import Calculator


def test_sum(monkeypatch: MonkeyPatch):
    def mock_sum(a, b):
        # mock sum function without the long running time.sleep
        return a + b

    monkeypatch.setattr("functions_mock.Calculator.sum", mock_sum)
    assert Calculator.sum(2, 3) == 5
    assert Calculator.sum(7, 3) == 10


def getssh():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"


def test_getssh(monkeypatch: MonkeyPatch):
    # mocked return function to replace Path.home
    # always return '/abc'
    def mockreturn():
        return Path("/abc")

    # Application of the monkeypatch to replace Path.home
    # with the behavior of mockreturn defined above.
    monkeypatch.setattr(Path, "home", mockreturn)

    # Calling getssh() will use mockreturn in place of Path.home
    # for this test with the monkeypatch.
    x = getssh()
    assert x == Path("/abc/.ssh")


# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_json(monkeypatch):

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = functions_mock.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
