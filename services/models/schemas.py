from pydantic import BaseModel


class AuthResponse(BaseModel):
    token: str


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str = None


class CreateBookingResponse(BaseModel):
    bookingid: int
    booking: Booking
