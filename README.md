# Roper Studio Booking App

## Version 2.0

Roper is a dark, studio-focused marketplace for discovering creative spaces,
checking availability, reserving a session, and managing bookings. Version 2.0
turns the original static clone into a complete Flask-powered booking journey.

This release was built and prepared by **Alains11**.

## What Changed In v2.0

### Product and branding

- Rebranded the experience from the original clone identity to Roper.
- Added a dark visual system across the header, hero, listings, detail pages,
	profile dashboard, confirmation screen, and footer.
- Added the studio-control-room hero background and studio marketplace styling.
- Removed stale legacy branding, external legacy images, and unresolved merge
	artifacts from the active and archived frontend pages.

### Studio discovery

- Added a live homepage search form for location, check-in, check-out, and
	guest count.
- Added location matching across studio names, descriptions, and city IDs.
- Added guest-capacity filtering before results are displayed.
- Preserved search dates and guest count when opening a studio detail page.
- Added responsive listing cards with studio images, descriptions, ratings, and
	nightly rates.

### Reservation flow

- Added studio detail pages with gallery, description, amenities, and booking
	form.
- Added native date selection with minimum-date and check-out constraints.
- Added guest-count validation against each studio's maximum capacity.
- Added live night count and total-price calculation.
- Added server-side validation for date format, date order, guest count, studio
	existence, and capacity.
- Added overlap protection so a studio cannot be booked twice for the same
	dates.
- Added a dedicated reservation confirmation page.

### Booking management

- Added file-backed Booking persistence through the existing model and storage
	layer.
- Added user-specific booking retrieval.
- Added a profile dashboard with studio names, dates, guest counts, status, and
	total price.
- Added confirmation links from the dashboard.
- Added cancellation support that preserves booking history with a `cancelled`
	status and releases the dates for future reservations.

### Reliability and maintenance

- Added demo users and studio listings when the store has no places.
- Added API and booking-flow regression tests.
- Resolved leftover merge conflicts in the console and README.
- Kept the console command prompt consistent with the Roper brand.

## Technology

- Python 3
- Flask
- Vanilla HTML, CSS, and JavaScript
- JSON file-backed storage
- Pytest

## Project Structure

```text
app.py                         Flask server and JSON API
console.py                     Local model command interpreter
models/                        Domain models and file storage engine
tests/                         Unit and booking-flow tests
web_static/index.html          Studio discovery homepage
web_static/property.html       Studio detail and reservation page
web_static/confirmation.html   Reservation confirmation page
web_static/profile.html        User booking dashboard
web_static/styles/main.css     Shared Roper visual system
file.json                      Local file-backed application data
```

## Run The App

From the repository root:

```bash
python3 app.py 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080) in a browser.

## Run The Tests

```bash
pytest -q
python3 -m py_compile app.py console.py models/*.py models/engine/*.py
```

The v2.0 suite covers model behavior, API search filtering, date validation,
capacity validation, and booking cancellation.

## API Routes

| Method | Route | Purpose |
| --- | --- | --- |
| `GET` | `/api/all` | Search studio listings by location and guest count |
| `GET` | `/api/all/Place` | Return all studios |
| `GET` | `/api/all/User` | Return stored users |
| `GET` | `/api/bookings/<user_id>` | Return a user's bookings |
| `POST` | `/api/bookings` | Create and persist a booking |
| `POST` | `/api/bookings/<booking_id>/cancel` | Cancel a booking while preserving its record |

## Console

The model console remains available for local storage work:

```bash
python3 console.py
```

The prompt is `(roper)` and supports the existing model commands, including
`help`, `quit`, `show`, `all`, `count`, `create`, `update`, and `destroy`.

## Release

Version: `2.0.0`

Author: **Alains11**

Repository: [atelier-concept-website](https://github.com/Alains11/atelier-concept-website)
