# Little Lemon Restaurant API

A comprehensive Django REST Framework API for managing a restaurant's menu items, bookings, and user authentication. This project provides a complete backend solution for a restaurant management system with user authentication, menu management, and booking functionality.

## Project Overview

The Little Lemon Restaurant API is built with Django and Django REST Framework, providing:
- **User Management**: Token-based authentication and user registration using Djoser
- **Menu Management**: Full CRUD operations for menu items
- **Booking System**: Manage restaurant reservations with authentication
- **Testing**: Comprehensive unit tests for models and API views
- **RESTful API**: Clean and intuitive API endpoints

## Features

### Authentication & Authorization
- Token-based authentication using Django REST Framework Token Authentication
- User registration and login endpoints via Djoser
- Protected endpoints requiring authentication
- Session-based authentication support

### API Endpoints

#### Menu Management
- `GET /restaurant/menu/` - List all menu items
- `POST /restaurant/menu/` - Create a new menu item
- `GET /restaurant/menu/<id>/` - Retrieve a specific menu item
- `PUT /restaurant/menu/<id>/` - Update a menu item
- `PATCH /restaurant/menu/<id>/` - Partially update a menu item
- `DELETE /restaurant/menu/<id>/` - Delete a menu item

#### Authentication
- `POST /auth/users/` - Register a new user
- `POST /auth/token/login/` - Obtain auth token
- `POST /auth/token/logout/` - Logout user
- `POST /restaurant/api-token-auth/` - Alternative token authentication endpoint

#### Bookings
- `GET /restaurant/booking/` - List all bookings (authenticated users only)
- `POST /restaurant/booking/` - Create a new booking (authenticated users only)
- `GET /restaurant/booking/<id>/` - Retrieve a specific booking
- `PUT /restaurant/booking/<id>/` - Update a booking
- `DELETE /restaurant/booking/<id>/` - Delete a booking

## Tech Stack

- **Backend**: Django 3.2+
- **API Framework**: Django REST Framework (DRF)
- **Authentication**: Django REST Framework Token Authentication + Djoser
- **Database**: SQLite (default), configurable for PostgreSQL/MySQL
- **Python Version**: 3.8+

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd LittleLemonFinal
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies using Pipenv**
   ```bash
   pipenv install
   pipenv shell
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://localhost:8000`

## Authentication Usage

### Register a New User
```bash
curl -X POST http://localhost:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "secure_password123",
    "email": "john@example.com"
  }'
```

### Obtain Authentication Token
```bash
curl -X POST http://localhost:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "secure_password123"
  }'
```

### Use Token in API Requests
```bash
curl -H "Authorization: Token YOUR_TOKEN_HERE" \
  http://localhost:8000/restaurant/menu/
```

## Database Models

### MenuItem
- `title` (CharField): Name of the menu item
- `price` (DecimalField): Price of the item
- `inventory` (SmallIntegerField): Stock quantity
- `__str__`: Returns formatted string "Title : Price"

### Booking
- `name` (CharField): Guest name
- `no_of_guests` (IntegerField): Number of guests
- `booking_date` (DateTimeField): Reservation date and time
- `__str__`: Returns guest name

## Testing

The project includes comprehensive unit tests for models and API views.

### Run All Tests
```bash
python manage.py test
```

### Run Tests for Specific App
```bash
python manage.py test tests.test_models
python manage.py test tests.test_views
```

### Run Tests with Verbose Output
```bash
python manage.py test --verbosity=2
```

### Test Coverage
- **Model Tests**: MenuItem creation and string representation
- **API View Tests**: Menu listing, filtering, and serialization
- **Authentication Tests**: Token-based authentication flows

## Project Structure

```
LittleLemonFinal/
├── littlelemon/              # Main project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
├── restaurant/              # Restaurant app
│   ├── models.py            # MenuItem and Booking models
│   ├── views.py             # API views and ViewSets
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # App-level URL routing
│   ├── admin.py             # Django admin configuration
│   ├── apps.py
│   └── migrations/          # Database migrations
├── tests/                   # Test suite
│   ├── test_models.py       # Model tests
│   └── test_views.py        # API view tests
├── static/                  # Static files (CSS, images)
├── templates/               # HTML templates
├── manage.py               # Django management script
├── Pipfile                 # Pipenv dependencies
├── Pipfile.lock            # Pipenv lock file
└── README.md               # This file
```

## Configuration

### Django Settings
Key configurations in `littlelemon/settings.py`:

```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'restaurant',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

DJOSER = {
    "USER_ID_FIELD": "username"
}
```

## API Response Examples

### List All Menu Items
**Request**: `GET /restaurant/menu/`

**Response**:
```json
[
  {
    "id": 1,
    "title": "IceCream",
    "price": "80.00",
    "inventory": 100
  },
  {
    "id": 2,
    "title": "Pizza",
    "price": "120.00",
    "inventory": 50
  }
]
```

### Create a Menu Item
**Request**: `POST /restaurant/menu/`

**Body**:
```json
{
  "title": "Pasta",
  "price": 95,
  "inventory": 30
}
```

**Response** (201 Created):
```json
{
  "id": 3,
  "title": "Pasta",
  "price": "95.00",
  "inventory": 30
}
```

## Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings.py
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Set a strong `SECRET_KEY`
- [ ] Use environment variables for sensitive configuration
- [ ] Switch to production-grade database (PostgreSQL recommended)
- [ ] Configure CORS settings appropriately
- [ ] Remove SessionAuthentication in production (use TokenAuthentication only)
- [ ] Set up HTTPS/SSL
- [ ] Configure static files serving
- [ ] Set up proper logging and error tracking
- [ ] Run security checks: `python manage.py check --deploy`

## Troubleshooting

### Migration Issues
```bash
python manage.py makemigrations
python manage.py migrate
```

### Reset Database
```bash
# Delete db.sqlite3 and migrations (except __init__.py)
python manage.py migrate
python manage.py createsuperuser
```

### Clear Cache
```bash
python manage.py clear_cache
```

## Environment Variables

Create a `.env` file in the project root:
```
SECRET_KEY=your_secret_key_here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See below for the full license text.

```
MIT License

Copyright (c) 2024 Little Lemon Restaurant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Author

Created as part of a Django REST Framework learning project.

## Support

For issues and questions, please open an issue on the GitHub repository.

## Future Enhancements

- [ ] Implement filtering and search on menu items
- [ ] Add pagination to list endpoints
- [ ] Implement user profiles and user management
- [ ] Add restaurant ratings and reviews
- [ ] Implement order management system
- [ ] Add payment integration
- [ ] Implement API documentation with Swagger/OpenAPI
- [ ] Add rate limiting
- [ ] Implement caching strategies

---

**Last Updated**: August 2026
