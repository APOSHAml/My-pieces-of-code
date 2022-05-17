import json
from urllib import error, request

import requests


def test_created_mem(base_url, authorization):
    url = f"{base_url}meme"
    headers = {
        "Content-Type": "application/json",
        "Authorization": authorization,
    }
    data = json.dumps(
        {
            "id": 22,
            "text": "kvaka",
            "url": "https://topmemas.top/img/img/1648455168.jpg",
            "tags": ["p1", "p2"],
            "info": {"i1": "mem1", "i2": "mem2"},
        }
    )
    response = requests.request("POST", url, headers=headers, data=data)
    response = json.loads(response.text)
    global ID_mem
    ID_mem = response["id"]
    

    assert response["text"] == "kvaka"


def test_update_put(base_url, authorization):
    req = request.Request(f"{base_url}meme/{ID_mem}")
    req.method = "PUT"
    req.add_header("Authorization", authorization)
    req.add_header("Content-Type", "application/json")
    req.data = json.dumps(
        {
            "id": int(ID_mem),
            "text": "kvaka N1",
            "url": "https://topmemas.top/img/img/1648455168.jpg",
            "tags": ["fun", "p2"],
            "info": {"i1": "mem1", "i2": "mem2"},
        }
    ).encode()
    response = json.loads((request.urlopen(req).read().decode("utf-8")))
    assert "kvaka N1" == response["text"]


def test_all_mems(authorization):
    req = request.Request("http://167.172.172.115:52353/meme")
    req.add_header("Authorization", authorization)
    response = request.urlopen(req).read().decode("utf-8")
    for ind in json.loads(response)["data"]:
        for keys in ind:
            if keys == "tags" and "fun" in ind["tags"]:
                return
    assert False


def test_delete_meme(base_url, authorization):
    req = request.Request(f"{base_url}meme/{ID_mem}")
    req.method = "DELETE"
    req.add_header("Authorization", authorization)
    request.urlopen(req)
    req = request.Request(f"{base_url}meme/{ID_mem}")
    try:
        req.add_header("Authorization", authorization)
        req = request.urlopen(req)
    except error.HTTPError as err:
        assert err.code == 404
        return

    assert False
