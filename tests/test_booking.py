import allure
from utils.data_generator import generate_booking_data
from services.models.schemas import CreateBookingResponse, Booking

@allure.feature("Booking")
def test_create_booking_success(api_client):
    data = generate_booking_data()
    response = api_client.post("/booking", data=data)
    assert response.status_code == 200
    CreateBookingResponse.parse_obj(response.json())

@allure.feature("Booking")
def test_get_booking_by_id(api_client):
    booking_id = 1
    response = api_client.get(f"/booking/{booking_id}")
    assert response.status_code == 200
    Booking.parse_obj(response.json())

@allure.feature("Booking")
def test_get_all_bookings(api_client):
    response = api_client.get("/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@allure.feature("Booking")
def test_update_booking(api_client):
    booking_id = 1
    data = generate_booking_data()
    response = api_client.put(f"/booking/{booking_id}", data=data)
    assert response.status_code == 200
    Booking.parse_obj(response.json())

@allure.feature("Booking")
def test_delete_booking(api_client):
    booking_id = 1
    response = api_client.delete(f"/booking/{booking_id}")
    assert response.status_code == 201 