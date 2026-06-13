import json

def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_home_returns_json(client):
    response = client.get("/")
    data = json.loads(response.data)
    assert "message" in data
    assert "version" in data

def test_home_message_contains_version(client, app_version):
    response = client.get("/")
    data = json.loads(response.data)
    assert app_version in data["message"]

def test_info_returns_200(client):
    response = client.get("/info")
    assert response.status_code == 200

def test_info_has_required_fields(client):
    response = client.get("/info")
    data = json.loads(response.data)
    assert "app"     in data
    assert "version" in data
    assert "env"     in data

def test_info_env_is_testing(client):
    response = client.get("/info")
    data = json.loads(response.data)
    assert data["env"] == "testing"

def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404