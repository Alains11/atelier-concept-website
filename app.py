from datetime import datetime
from flask import Flask, jsonify, request, send_from_directory
import models
import os

app = Flask(__name__, static_folder='web_static')


def serialize_objects(objects):
    """Serialize storage objects keyed by their id."""
    serialized = {}
    for obj in objects.values():
        if hasattr(obj, 'to_dict'):
            payload = obj.to_dict()
            serialized[payload.get('id', str(obj))] = payload
    return serialized


def seed_demo_data():
    """Create a default user and sample studio listings if the store is empty."""
    all_objs = models.storage.all()
    if any(obj.__class__.__name__ == 'Place' for obj in all_objs.values()):
        return

    from models.place import Place
    from models.user import User

    demo_user = User()
    demo_user.name = 'Avery Stone'
    demo_user.email = 'avery@roper.studio'
    demo_user.password = 'demo-password'
    models.storage.new(demo_user)

    studio_samples = [
        {
            'name': 'Sunset Loop Studio',
            'description': 'A bright rehearsal space with live room acoustics and a vintage drum kit.',
            'price_by_night': 180,
            'max_guest': 6,
            'number_rooms': 2,
            'number_bathrooms': 1,
            'city_id': 'sf',
            'user_id': demo_user.id,
        },
        {
            'name': 'Harbor Session Loft',
            'description': 'A modern music studio with an upright piano, vocal booth, and producer desk.',
            'price_by_night': 240,
            'max_guest': 8,
            'number_rooms': 3,
            'number_bathrooms': 2,
            'city_id': 'sf',
            'user_id': demo_user.id,
        },
        {
            'name': 'Midnight Echo Room',
            'description': 'A moody creative suite built for recording, mixing, and intimate performances.',
            'price_by_night': 210,
            'max_guest': 5,
            'number_rooms': 2,
            'number_bathrooms': 1,
            'city_id': 'la',
            'user_id': demo_user.id,
        },
    ]

    for studio in studio_samples:
        place = Place()
        for key, value in studio.items():
            setattr(place, key, value)
        models.storage.new(place)

    models.storage.save()


models.storage.reload()
seed_demo_data()

# Serve the static frontend
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

# API Endpoints
@app.route('/api/all', methods=['GET'])
def get_all():
    """Returns all objects from storage"""
    all_objs = models.storage.all()
    location = request.args.get('location', '').strip()
    filtered = []
    for obj in all_objs.values():
        if obj.__class__.__name__ != 'Place':
            continue
        if not location or location.lower() == 'anywhere' or location.lower() in (obj.name or '').lower():
            filtered.append(obj)

    data = serialize_objects({obj.id: obj for obj in filtered})
    return jsonify(data)

@app.route('/api/all/<cls>', methods=['GET'])
def get_all_by_class(cls):
    """Returns all objects of a specific class"""
    all_objs = models.storage.all()
    objects = [v for v in all_objs.values() if v.__class__.__name__ == cls]
    data = serialize_objects({obj.id: obj for obj in objects})
    return jsonify(data)

@app.route('/api/bookings/<user_id>', methods=['GET'])
def get_user_bookings(user_id):
    """Returns all bookings for a specific user"""
    all_objs = models.storage.all()
    user_bookings = [v for v in all_objs.values()
                    if v.__class__.__name__ == 'Booking' and v.user_id == user_id]

    data = serialize_objects({obj.id: obj for obj in user_bookings})
    return jsonify(data)

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Creates a new studio booking"""
    data = request.get_json(silent=True) or {}

    required = ['user_id', 'place_id', 'check_in', 'check_out']
    if not all(k in data for k in required):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        check_in = datetime.strptime(data['check_in'], '%Y-%m-%d').date()
        check_out = datetime.strptime(data['check_out'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Dates must use YYYY-MM-DD format"}), 400

    if check_out <= check_in:
        return jsonify({"error": "Check-out must be after check-in"}), 400

    guest_count = int(data.get('guest_count', 1))
    if guest_count < 1:
        return jsonify({"error": "Guest count must be at least 1"}), 400

    all_objs = models.storage.all()
    place = next((obj for obj in all_objs.values() if obj.__class__.__name__ == 'Place' and obj.id == data['place_id']), None)
    nightly_rate = 0.0
    if place is not None:
        nightly_rate = float(getattr(place, 'price_by_night', getattr(place, 'price_per_night', 0.0)))

    nights = max(1, (check_out - check_in).days)
    total_price = nightly_rate * nights

    from models.booking import Booking
    new_booking = Booking()
    for key, value in data.items():
        setattr(new_booking, key, value)

    new_booking.name = f"Studio booking for {data['user_id']}"
    new_booking.check_in = data['check_in']
    new_booking.check_out = data['check_out']
    new_booking.guest_count = guest_count
    new_booking.total_price = total_price
    new_booking.status = 'confirmed'

    models.storage.new(new_booking)
    models.storage.save()

    return jsonify(new_booking.to_dict()), 201

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host='0.0.0.0', port=port, debug=True)
