import json
from app import app

def test_valid_input():
    client = app.test_client()
    response = client.post('/transform',
                           data=json.dumps({"voltage": 2}),
                           content_type='application/json')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["temperature"] == 20

def test_missing_voltage():
    client = app.test_client()
    response = client.post('/transform',
                           data=json.dumps({}),
                           content_type='application/json')

    assert response.status_code == 400

def test_invalid_voltage():
    client = app.test_client()
    response = client.post('/transform',
                           data=json.dumps({"voltage": "abc"}),
                           content_type='application/json')

    assert response.status_code == 400