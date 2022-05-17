import json
from urllib import request

import pytest
import requests


@pytest.fixture(scope="session")
def authorization():
    url = "http://167.172.172.115:52353/authorize"
    data = json.dumps({"name": "Siarhei"})
    headers = {"name": "Siarhei"}
    try:
        with open("token.txt", "r") as h:
            cod = h.read()
            actual_token = requests.request(
                "GET", f"{url}/{cod}", headers=headers, data=data
            )

            if actual_token.status_code == 404:
                headers = {"Content-Type": "application/json"}
                response = requests.request("POST", url, headers=headers, data=data)
                response = response.json()
                valid_token = requests.request(
                    "GET",
                    f"{url}/" + response["token"],
                    headers=headers,
                    data=data,
                )
                assert "Token is alive. Username is Siarhei" == valid_token.text
                with open("token.txt", "w") as h:
                    h.write(response["token"])
                with open("token.txt", "r") as h:
                    cod = h.read()

                return cod
            return cod
    except Exception as f:
        raise f


@pytest.fixture(scope="function")
def base_url():
    yield "http://167.172.172.115:52353/"

