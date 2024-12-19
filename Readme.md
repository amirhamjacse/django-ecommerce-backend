# Django eCommerce Backend

This is the backend for an eCommerce application built with **Django** and **Django Rest Framework (DRF)**. It provides RESTful APIs for managing products, categories, user authentication, orders, and payments.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Set Up Database](#set-up-database)
  - [Create Superuser](#create-superuser)
- [API Documentation](#api-documentation)
  - [Authentication](#authentication)
  - [Product Endpoints](#product-endpoints)
  - [Order Endpoints](#order-endpoints)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This Django eCommerce backend provides RESTful APIs to manage the core features of an eCommerce application, including:

- **User Authentication**: Registration, login, and user profile management.
- **Product Management**: CRUD operations for products, categories, and product attributes.
- **Order Management**: Create, update, and view orders.
- **Payment Integration**: Integration with a payment gateway (if applicable, e.g., Stripe or PayPal).

This project is built using Django, Django Rest Framework, and is structured to be modular and extendable.

---

## Technologies Used

- **Django** - A high-level Python web framework.
- **Django Rest Framework (DRF)** - A powerful toolkit for building Web APIs in Django.
- **PostgreSQL/MySQL** - Relational database management system.
- **Docker** (optional) - For containerization and easy deployment.
- **Stripe/PayPal** (optional) - For payment processing.

---

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/django-ecommerce-backend.git
cd django-ecommerce-backend
```

### Create a Virtual Environment

Create and activate a virtual environment to isolate your dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Set Up Database

Ensure you have a database setup (PostgreSQL/MySQL). If you're using PostgreSQL, you may need to install PostgreSQL locally or use a Docker container. Update the `DATABASES` settings in `settings.py` to match your database credentials.

Run the migrations to set up your database schema:

```bash
python manage.py migrate
```

### Create Superuser

To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

## API Documentation

### Authentication

- **Register**: `POST /api/auth/register/`  
  Register a new user.

  **Request Body**:
  ```json
  {
    "username": "newuser",
    "email": "user@example.com",
    "password": "password123"
  }
  ```

- **Login**: `POST /api/auth/login/`  
  Login and obtain an authentication token.

  **Request Body**:
  ```json
  {
    "username": "user",
    "password": "password123"
  }
  ```

  **Response**:
  ```json
  {
    "token": "your_jwt_token"
  }
  ```

### Product Endpoints

- **List Products**: `GET /api/products/`  
  Get a list of all products. You can also filter by category, price, etc.

- **Create Product**: `POST /api/products/`  
  Create a new product (admin only).

  **Request Body**:
  ```json
  {
    "name": "Product Name",
    "description": "Product Description",
    "price": 29.99,
    "category": 1  # Category ID
  }
  ```

- **Update Product**: `PUT /api/products/{id}/`  
  Update a product's details (admin only).

- **Delete Product**: `DELETE /api/products/{id}/`  
  Delete a product (admin only).

### Order Endpoints

- **Create Order**: `POST /api/orders/`  
  Create an order.

  **Request Body**:
  ```json
  {
    "product_ids": [1, 2, 3],
    "user": 1,
    "total_price": 99.99
  }
  ```

- **Get Order Details**: `GET /api/orders/{id}/`  
  Retrieve details of a specific order.

---

## Testing

To run the tests for this project, ensure that you have the necessary dependencies installed and run:

```bash
python manage.py test
```

The test suite will automatically discover and run all the tests in your `tests.py` files.

---

## Deployment

### Using Docker (Optional)

1. **Build the Docker image**:
   ```bash
   docker build -t django-ecommerce-backend .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d -p 8000:8000 django-ecommerce-backend
   ```

3. You can now access the app by visiting `http://localhost:8000`.

### Heroku Deployment (Optional)

You can deploy this project to Heroku by following these steps:

1. Create a `Procfile`:
   ```txt
   web: gunicorn ecommerce_backend.wsgi
   ```

2. Push the code to Heroku and deploy as usual:
   ```bash
   git push heroku master
   ```

---

## Contributing

Contributions are welcome! If you have a bug fix, new feature, or documentation improvement, please feel free to submit a pull request. Make sure to follow the [contribution guidelines](CONTRIBUTING.md).

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:

1. You can modify the `ProductSerializer`, `OrderSerializer`, etc., based on your exact requirements (like adding stock quantity, discounts, etc.).
2. For payment integration, you'll need to set up **Stripe** or **PayPal** APIs depending on your chosen service and modify the order endpoints accordingly.
3. Update the URLs and settings for the `ecommerce_backend` project as needed based on your project structure.

