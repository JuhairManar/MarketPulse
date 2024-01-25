[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![Django Version](https://img.shields.io/badge/Django-3.2-green)
![Django Rest Framework Version](https://img.shields.io/badge/Django%20Rest%20Framework-3.12-green)

MarketPulse is a Django-based project designed for managing and reviewing products with a focus on user engagement. It provides a RESTful API powered by Django Rest Framework, enabling seamless interaction with your product database.

## Features

- **User Authentication:** Secure user registration and login with token-based authentication.
- **Product Management:** CRUD operations for managing products, including details like name, description, and price.
- **Product Reviews:** Allow users to review and rate products, creating a dynamic feedback system.
- **Admin Controls:** Admin-only access for critical operations, ensuring control over product listings.
- **Pagination:** Implement paginated views for a smoother user experience.
- **Advanced Filtering:** Filter products and reviews by user, rating, and product name.
- **Token-Based Authentication:** Secure API access with token-based authentication.
- **Logout Functionality:** Provide a simple endpoint for users to log out.

## Getting Started

These instructions will guide you to set up the MarketPulse project locally. Ensure you have Python 3.9 or higher installed.

### Prerequisites

- Python 3.9 or higher
- Django 3.2
- Django Rest Framework
- ...

### Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
