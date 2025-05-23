from faker import Faker

fake = Faker()

def generate_booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=50, max=500),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": fake.date_this_year().isoformat(),
            "checkout": fake.date_this_year().isoformat(),
        },
        "additionalneeds": fake.word()
    } 