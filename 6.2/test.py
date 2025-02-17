from reservation_system import Hotel, Customer, Reservation


def test_hotel():
    try:
        Hotel.create_hotel(1, "Hotel Central", "Rurrenabaque", 50)
        Hotel.create_hotel(2, "Hotel Plaza", "Choquechaca", 100)
        Hotel.create_hotel(None, "Barranca", "Quillacollo", 30)
    except Exception as e:
        print(f"Error creating valid hotels: {e}")


def test_customer():
    try:
        Customer.create_customer(1, "Riquelme", "rop@example.com")
        Customer.create_customer(2, "Christian Arabe", "capo@example.com")
        Customer.create_customer(None, "Invalid Customer", "invalid@example.com")
    except Exception as e:
        print(f"Error creating valid customers: {e}")


def test_reservation():
    try:
        Reservation.create_reservation(1, 1, 1)
        Reservation.create_reservation(2, 1, 2)
        Reservation.create_reservation(None, 1, 2)
    except Exception as e:
        print(f"Error creating valid reservations: {e}")


if __name__ == "__main__":
    test_hotel()
    test_customer()
    test_reservation()
