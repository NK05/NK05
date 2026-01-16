# Purple Seeds Solutions Marketplace MVP

## Run locally

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
```

## Purpose
- Demonstrate marketplace flow:
  **Login → Portal → Marketplace → Solution → Customize → Deploy → Support**
- No product backend, no APIs, no payments
- Suitable for demos, validation, and stakeholder walkthroughs

## Tech Stack
- Python 3.11+
- Django (auth + templates only)
- TailwindCSS (CDN)
- Alpine.js (light interactivity)
- Mock catalog data (Python)
- Quote requests stored as JSON

## Demo login
- username: demo
- password: demo12345

## Mocked data
- Catalog data lives in `marketplace/services/catalog.py`.
- Quote requests append to `storage/quote_requests.json`.

## Notes
- No product database models are created for solutions/tiers/add-ons/quotes.
- All pages except `/login/` require authentication.
