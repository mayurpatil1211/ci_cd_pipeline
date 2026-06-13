import json

def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_health_returns_ok_status(client):
    response = client.get("/health")
    data = json.loads(response.data)
    assert data["status"] == "ok"

def test_health_includes_version(client, app_version):
    response = client.get("/health")
    data = json.loads(response.data)
    assert data["version"] == app_version

def test_health_is_json(client):
    response = client.get("/health")
    assert response.content_type == "application/json"