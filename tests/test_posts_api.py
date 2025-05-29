import requests
import pytest

@pytest.mark.smoke
def test_get_all_posts(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 100  # JSONPlaceholder returns 100 posts

@pytest.mark.regression
def test_get_single_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
