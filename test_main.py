import pytest
import socket as s
import requests
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Инициализирует серверный сокет
@pytest.yield_fixture
def socket():
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    yield _socket
    _socket.close()


# Проверка установленного соединения с сервером
def test_server_connect(socket):
    socket.connect(('0.0.0.0', 8000))
    assert socket


# Проверка данных из корня программы
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


# Проверка на идентичность данных полученных из БД и в следствии запроса по API
def test_read_item():
    response = client.get("/employees/")
    employees = []
    with open("employees.json", 'r') as f:
        for line in f:
            employees.append(line)
    assert response.status_code == 200
    assert response.json() == {'list_employees': employees}


# Проверка, неверно указанного адреса, получения данных
def test_read_inexistent_item():
    response = client.get("/employee/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
