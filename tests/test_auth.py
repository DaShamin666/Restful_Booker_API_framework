import pytest
import allure
from services.models.schemas import AuthResponse

@allure.feature("Auth")
@pytest.mark.parametrize("username,password,expected_status", [
    ("admin", "password123", 200),
    ("admin", "wrongpass", 200),
    ("", "", 200),
    ("", "password123", 200),
    ("admin", "", 200),
])
def test_auth(api_client, username, password, expected_status):
    with allure.step("Отправка запроса на авторизацию"):
        response = api_client.post("/auth", data={"username": username, "password": password})
    assert response.status_code == expected_status
    if username == "admin" and password == "password123":
        AuthResponse.parse_obj(response.json())
    else:
        assert "token" not in response.json() 