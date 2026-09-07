#!/usr/bin/python3
"""
Module Booking defines the Booking class
"""
from models.base_model import BaseModel
from datetime import datetime


class Booking(BaseModel):
    """
    Class to represent a studio booking
    """

    name = ""
    user_id = ""
    place_id = ""
    check_in = ""
    check_out = ""
    total_price = 0.0
    status = "confirmed"  # confirmed, cancelled, pending

    def __init__(self, *args, **kwargs):
        """Initializes a new Booking object"""
        super().__init__(*args, **kwargs)
