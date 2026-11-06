import os

import pytest
import requests

BASE = os.environ.get("API_BASE_URL", "https://jsonplaceholder.typicode.com")
TIMEOUT = 10


@pytest.mark.api
def test_get_single_post_has_expected_fields():
    res = requests.get(f"{BASE}/posts/1", timeout=TIMEOUT)
    assert res.status_code == 200
    assert {"userId", "id", "title", "body"} <= res.json().keys()


@pytest.mark.api
def test_list_posts_returns_100():
    res = requests.get(f"{BASE}/posts", timeout=TIMEOUT)
    assert res.status_code == 200
    assert len(res.json()) == 100


@pytest.mark.api
def test_filter_posts_by_user():
    res = requests.get(f"{BASE}/posts", params={"userId": 1}, timeout=TIMEOUT)
    assert res.status_code == 200
    assert all(post["userId"] == 1 for post in res.json())


@pytest.mark.api
def test_create_post_echoes_payload():
    payload = {"title": "hello", "body": "world", "userId": 1}
    res = requests.post(f"{BASE}/posts", json=payload, timeout=TIMEOUT)
    assert res.status_code == 201
    assert res.json()["title"] == "hello"


@pytest.mark.api
def test_missing_post_is_404():
    res = requests.get(f"{BASE}/posts/99999", timeout=TIMEOUT)
    assert res.status_code == 404
