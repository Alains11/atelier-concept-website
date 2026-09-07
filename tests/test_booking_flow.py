#!/usr/bin/python3
"""Tests for booking validation behavior."""

from app import app


def test_create_booking_rejects_invalid_date_range():
    """Bookings should reject check-out dates that happen before check-in."""
    client = app.test_client()
    response = client.post(
        '/api/bookings',
        json={
            'user_id': 'demo-user',
            'place_id': 'studio-1',
            'check_in': '2026-09-10',
            'check_out': '2026-09-08',
            'guest_count': 2,
        },
    )

    assert response.status_code == 400
    payload = response.get_json()
    assert 'Check-out must be after check-in' in payload['error']
