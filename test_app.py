from app import app, FORTUNES


def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_api_returns_valid_fortune():
    client = app.test_client()
    r = client.get("/api/fortune")
    assert r.status_code == 200
    assert r.get_json()["fortune"] in FORTUNES


def test_home_page():
    client = app.test_client()
    assert client.get("/").status_code == 200
