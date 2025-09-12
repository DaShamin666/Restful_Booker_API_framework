import pytest
import allure
from utils.data_generator import generate_booking_data
from services.models.schemas import CreateBookingResponse, Booking

class TestBooking:
    @allure.feature("Booking")
    def test_create_booking_success(self, api_client):
        data = generate_booking_data()
        response = api_client.post("/booking", data=data)
        assert response.status_code == 200
        CreateBookingResponse.model_validate(response.json())

    def test_get_booking_by_id(self, api_client):
        booking_id = 1
        response = api_client.get(f"/booking/{booking_id}")
        assert response.status_code == 200
        Booking.model_validate(response.json())

    def test_get_all_bookings(self, api_client):
        response = api_client.get("/booking")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_update_booking(self, api_client):
        booking_id = 1
        data = generate_booking_data()
        response = api_client.put(f"/booking/{booking_id}", data=data)
        assert response.status_code == 200
        Booking.model_validate(response.json())

    def test_delete_booking(self, api_client):
        booking_id = 1
        response = api_client.delete(f"/booking/{booking_id}")
        assert response.status_code == 201