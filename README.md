# Amnify Appointment Booking System

This is a Django + GraphQL project that allows creating, viewing, and canceling appointments.

## Features

- Create new appointments using GraphQL mutation
- Cancel existing appointments by ID
- View all appointments with their statuses
- GraphQL interface available at /cleaning/graphql/


## How to Run Locally

1. Clone the repository

git clone https://github.com/rahulp2020/AmnifyProject.git
cd AmnifyProject

2. Create a virtual environment and activate it

On Windows:
python -m venv venv
venv\Scripts\activate

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py makemigrations
python manage.py migrate

5. Create superuser (optional)

python manage.py createsuperuser

6. Run the development server

python manage.py runserver

Visit http://127.0.0.1:8000/cleaning/graphql/ to access the GraphQL playground

## Example GraphQL Queries

Get all appointments:

query {
  allAppointments {
    id
    time
    status
    createdAt
    updatedAt
  }
}

Create a new appointment:

mutation {
  createAppointment(time: "2025-08-01T14:00:00Z") {
    appointment {
      id
      time
      status
    }
  }
}

Cancel an appointment:

mutation {
  cancelAppointment(id: 1) {
    success
  }
}

## Notes

- Make sure time is passed in ISO 8601 format (UTC)
- Admin panel is available at http://127.0.0.1:8000/admin/

