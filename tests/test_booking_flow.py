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


def test_search_can_filter_by_guest_capacity():
    """Search should omit studios that cannot fit the requested group."""
    client = app.test_client()
    response = client.get('/api/all?guests=99')

    assert response.status_code == 200
    assert response.get_json() == {}


def test_cancel_booking_marks_booking_without_deleting_it():
    """Cancellation should preserve the booking record with a cancelled status."""
    client = app.test_client()
    places = client.get('/api/all/Place').get_json()
    place_id = next(iter(places))
    created = client.post(
        '/api/bookings',
        json={
            'user_id': 'demo-user',
            'place_id': place_id,
            'check_in': '2030-01-10',
            'check_out': '2030-01-12',
            'guest_count': 1,
        },
    )

    assert created.status_code == 201
    booking_id = created.get_json()['id']
    cancelled = client.post(f'/api/bookings/{booking_id}/cancel')

    assert cancelled.status_code == 200
    assert cancelled.get_json()['status'] == 'cancelled'
