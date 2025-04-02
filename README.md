# Music Booking App

Music booking api designed for event organizers to create events and invite artists. The app allows users to manage event details, artist availability, and artist bookings for events. It also provide endpoint for users to book an event

## Features
- **Event Management**: Create and manage events with location, date, and pricing.
- **Booking Management**: Book events, get booking transactions
- **Artist Management**: Add and manage artists for events
- **User Authentication**: Register and login for both event organizers and artists.

## Setup and Run Locally

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- pip (Python package installer)
- Git

### Steps to Set Up

1. **Clone the Repository**  
   Clone the project to your local machine:
   ```bash
   git clone https://github.com/Razkky/music-booking-api.git
   cd music-booking-api
   
2. **Create a Virtual Environment**__
    Create virtual environment and activate it
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**
   Install the required dependencies
   ```bash
   pip install -r requirements.txt

4. **Run migrations**
   Apply database migrations
   ```bash
   python manage.py migrate

5. **Seed genres**
   Seed default music genres
   ```bash
   python manage.py shell
   from user.seeder.genre import main
   main()

6. **Run the development server**
   ```bash
   python manage.py runserver
   
### API Documentation
For detailed documentation and usage instruction, refer to the full [documentation](https://documenter.getpostman.com/view/34067711/2sB2cSfhky#7b9cf3ce-aa1d-4b6e-bf8f-01904b9a1d96)

   



