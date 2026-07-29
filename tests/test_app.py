import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
)

from app import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Automated AWS CI/CD Pipeline" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    response_data = response.get_json()

    assert response.status_code == 200
    assert response_data["status"] == "healthy"
    assert response_data["service"] == "aws-docker-cicd-webapp"
    assert response_data["region"] == "eu-central-1"