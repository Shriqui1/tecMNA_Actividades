"""
Hotel Reservation System Module

This module provides three classes: Hotel, Customer, and Reservation.
Each class allows for creating, modifying, deleting, and retrieving
records stored in JSON files.
"""
import json
import os


class Hotel:
    """
    Represents a hotel with attributes
    like ID, name, location, and available rooms.
    """
    FILE_PATH = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms):
        if not hotel_id or not isinstance(hotel_id, int):
            print("Invalid hotel ID.")
            return
        if not name or not isinstance(name, str):
            print("Invalid hotel name.")
            return
        if not location or not isinstance(location, str):
            print("Invalid hotel location.")
            return
        if rooms is None or not isinstance(rooms, int):
            print("Invalid available rooms value.")
            return
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """Converts the hotel instance to a dictionary."""
        return self.__dict__

    @classmethod
    def save_to_file(cls, hotels):
        """Saves the list of hotels to a JSON file."""
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([hotel.to_dict() for hotel in hotels
                       if isinstance(hotel, Hotel)], file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Loads data from a JSON file and returns a list of Hotels."""
        if not os.path.exists(cls.FILE_PATH):
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [cls(**hotel) for hotel in data
                        if isinstance(hotel, dict)]
        except (json.JSONDecodeError, FileNotFoundError) as error:
            print(f"Error loading hotel data: {error}")
            return []

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms):
        """Creates and saves a new hotel."""
        try:
            new_hotel = cls(hotel_id, name, location, rooms)
            if isinstance(new_hotel, Hotel):
                hotels = cls.load_from_file()
                hotels.append(new_hotel)
                cls.save_to_file(hotels)
        except ValueError as error:
            print(f"Error creating hotel: {error}")

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Deletes a hotel by its ID."""
        hotels = [hotel for hotel in cls.load_from_file()
                  if hotel.hotel_id != hotel_id]
        cls.save_to_file(hotels)

    @classmethod
    def modify_hotel(cls, hotel_id, name=None,
                     location=None, rooms=None):
        """Modifies the attributes of a hotel."""
        hotels = cls.load_from_file()
        for hotel in hotels:
            if hotel.hotel_id == hotel_id:
                if name:
                    hotel.name = name
                if location:
                    hotel.location = location
                if rooms is not None:
                    hotel.rooms = rooms
        cls.save_to_file(hotels)

    @classmethod
    def display_hotels(cls):
        """Returns a list of all hotels."""
        return cls.load_from_file()


class Customer:
    """
    Represents a customer with attributes like ID, name, and email.
    """
    FILE_PATH = "customers.json"

    def __init__(self, customer_id, name, email):
        if not customer_id or not name or not email:
            raise ValueError("All customer attributes must be provided.")
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Converts the customer instance to a dictionary."""
        return self.__dict__

    @classmethod
    def save_to_file(cls, customers):
        """Saves the list of customers to a JSON file."""
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([customer.to_dict() for customer in customers
                       if isinstance(customer, Customer)], file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Loads data from a JSON file and returns a list of Customers."""
        if not os.path.exists(cls.FILE_PATH):
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [cls(**customer) for customer in data]
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error loading customer data.")
            return []

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Creates and saves a new customer."""
        try:
            new_customer = cls(customer_id, name, email)
            if isinstance(new_customer, Customer):
                customers = cls.load_from_file()
                customers.append(new_customer)
                cls.save_to_file(customers)
        except ValueError as error:
            print(f"Error creating customer: {error}")

    @classmethod
    def delete_customer(cls, customer_id):
        """Deletes a customer by their ID."""
        customers = [customer for customer in cls.load_from_file()
                     if customer.customer_id != customer_id]
        cls.save_to_file(customers)

    @classmethod
    def display_customers(cls):
        """Returns a list of all customers."""
        return cls.load_from_file()


class Reservation:
    """
    Represents a reservation with attributes
    like reservation ID, customer ID, and hotel ID.
    """
    FILE_PATH = "reservations.json"

    def __init__(self, reservation_id, customer_id, hotel_id):
        if not reservation_id or not customer_id or not hotel_id:
            raise ValueError("All reservation attributes must be provided.")
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Converts the reservation instance to a dictionary."""
        return self.__dict__

    @classmethod
    def save_to_file(cls, reservations):
        """Saves the list of reservations to a JSON file."""
        with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([res.to_dict() for res in reservations], file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Loads data from a JSON file and returns a list of Reservations."""
        if not os.path.exists(cls.FILE_PATH):
            return []
        try:
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [cls(**res) for res in data]
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error loading reservation data.")
            return []

    @classmethod
    def create_reservation(cls, reservation_id, customer_id, hotel_id):
        """Creates and saves a new reservation."""
        reservations = cls.load_from_file()
        reservations.append(cls(reservation_id, customer_id, hotel_id))
        cls.save_to_file(reservations)

    @classmethod
    def cancel_reservation(cls, reservation_id):
        """Cancels a reservation by its ID."""
        reservations = [res for res in cls.load_from_file()
                        if res.reservation_id != reservation_id]
        cls.save_to_file(reservations)
