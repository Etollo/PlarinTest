import pytest
import socket as s
import requests
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.yield_fixture
def socket():
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    yield _socket
    _socket.close()


def test_server_connect(socket):
    socket.connect(('0.0.0.0', 8000))
    assert socket


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_read_item():
    response = client.get("/employees/")
    employees = []
    with open("employees.json", 'r') as f:
        for line in f:
            employees.append(line)
    assert response.status_code == 200
    assert response.json() == {'list_employees': employees}


def test_read_inexistent_item():
    response = client.get("/employee/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
