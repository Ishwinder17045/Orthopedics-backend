# Ortho Backend

Backend API for the orthopedic healthcare website. It provides doctors, services, appointments, contact messages, testimonials, orthopedic news, and user authentication.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- MySQL-compatible database via PyMySQL
- Pydantic
- JWT authentication with `python-jose`
- Password hashing with Passlib
- NewsAPI integration

## Project Structure

```text
ortho-backend/
+-- database/          # Database connection and session setup
+-- models/            # SQLAlchemy models
+-- routes/            # FastAPI route modules
+-- schemas/           # Pydantic request/response schemas
+-- services/          # External service integrations
+-- utils/             # Auth and shared helpers
+-- main.py            # FastAPI app entry point
+-- seed.py            # Initial seed data
+-- requirements.txt   # Python dependencies
+-- start.sh           # Deployment start command
```

## Prerequisites

- Python 3.10+
- MySQL or a MySQL-compatible database
- NewsAPI key, if you want live orthopedic news

## Setup

1. Clone the repository and move into the backend folder:

```bash
cd ortho-backend
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend root:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/database_name
SECRET_KEY=replace-with-a-secure-random-secret
NEWS_API_KEY=your-newsapi-key
```

Do not commit your `.env` file to GitHub.

## Running Locally

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Deployment

The included `start.sh` runs the app with Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Make sure your deployment platform provides:

- `DATABASE_URL`
- `SECRET_KEY`
- `NEWS_API_KEY`
- `PORT`

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Health check message |
| `POST` | `/auth/signup` | Register a new user |
| `POST` | `/auth/login` | Log in and receive a bearer token |
| `GET` | `/auth/me` | Get the current authenticated user |
| `GET` | `/doctors/` | List available doctors |
| `GET` | `/doctors/{doctor_id}` | Get a single doctor |
| `GET` | `/services/` | List services |
| `GET` | `/services/{service_id}` | Get a single service |
| `POST` | `/appointments/` | Create an appointment |
| `GET` | `/appointments/` | List appointments, optionally filtered by doctor or status |
| `GET` | `/appointments/{appointment_id}` | Get a single appointment |
| `POST` | `/contact/` | Submit a contact message |
| `GET` | `/testimonials/` | List testimonials |
| `GET` | `/news/` | Fetch orthopedic news articles |
| `GET` | `/news/health` | Check NewsAPI health |

## Database Notes

On startup, `main.py` creates database tables from the SQLAlchemy models and runs `seed_initial_data()` from `seed.py`.

Before running the server, make sure:

- The database exists.
- `DATABASE_URL` points to the correct database.
- The database user has permission to create tables and insert seed data.

## CORS

The API currently allows local frontend origins including:

- `http://localhost:3000`
- `http://127.0.0.1:3000`
- `http://localhost:5173`
- `http://127.0.0.1:5173`
- `http://localhost:5175`
- `http://127.0.0.1:5175`

Update the CORS settings in `main.py` before deploying with a production frontend domain.

## Security Notes

- Use a strong `SECRET_KEY` in production.
- Keep `.env` out of version control.
- Rotate any exposed API keys or database credentials.
- Restrict CORS origins for production.
