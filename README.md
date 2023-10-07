# Phase 5 Capstone Project - Travel App

## About

Travel App is a web application that allows users to record and explore their travel experiences.


## Overview

Travel App is designed to help users keep track of their travel memories, including visited cities, best experiences, and accommodation details. Users can also connect with other travelers and share their travel stories.


## Features

Some of the features of this app include:

- User Authentication: Users can log in to the application.
- City Creation: Users can create entries for cities they have visited.
- City Listing: Users can view a list of cities they have added.
- City Details: Users can view details of a specific city, including best memories and accommodation.


## Installation

1. Clone the repository: git clone https://github.com/ErnestWinata/capstone-project

2. Navigate to the server directory: cd server

3. Install backend dependencies: pip install

4. Set up the database:
- Create a database: python manage.py db init
- Migrate the database: python manage.py db migrate
- Apply the migrations: python manage.py db upgrade

5. Run the backend server: python app.py
   
6. Navigate to the client directory: cd client
   
7. Install frontend dependencies: npm install

8. Run the frontend server: npm start


## Usage

1. Visit the application at http://localhost:3000 in your web browser.
2. Create an account or log in using the provided options.
3. Add cities you have visited and explore the app's features.


## API Endpoints

POST /cities: Create a new city.

GET /cities: Get a list of all cities.

GET /cities/<city_id>: Get details of a specific city.

DELETE /cities/<city_id>: Delete a city.


## Tools and Libraries Used

- Flask: Web application framework for the backend.
- React: JavaScript library for building the frontend user interface.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) for Python.


## License

This project is licensed under the MIT License.
