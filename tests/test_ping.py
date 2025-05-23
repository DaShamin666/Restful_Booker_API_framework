import allure

@allure.feature("Ping")
def test_ping(api_client):
    response = api_client.get("/ping")
    assert response.status_code == 201
    assert response.text == "Created" 