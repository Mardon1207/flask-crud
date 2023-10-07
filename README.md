# Product Management API Documentation

Welcome to the Product Management API documentation. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on products within your system. Whether you are building an e-commerce platform or a simple inventory management system, this API can help you manage your products efficiently.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Endpoints](#endpoints)
3. [API Details](#api-details)
4. [Project File Structure](#project-file-structure)

## Getting Started
To get started with this API, you do not need authentication. Simply use the base URL below to access the API.

Base URL: `https://localhost:500/api/v1`

## Endpoints

| Endpoint               | Method | Description                                  | Request Body (JSON)                                                  | Response                                                      |
|------------------------|--------|----------------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------|
| `/products`            | POST   | Create a Product                             | ``` {"name": "Product Name", "description": "Product Description", "price": 19.99, "quantity": 100} ``` | 201 Created, 400 Bad Request                                  |
| `/products/{product_id}` | GET    | Read a Product                               | -                                                                     | 200 OK, 404 Not Found                                       |
| `/products/{product_id}` | PUT    | Update a Product                             | ``` {"name": "New Product Name", "description": "New Product Description", "price": 24.99, "quantity": 75} ``` | 200 OK, 400 Bad Request, 404 Not Found                       |
| `/products/{product_id}` | DELETE | Delete a Product                             | -                                                                     | 204 No Content, 404 Not Found                               |
| `/products`            | GET    | List All Products                            | -                                                                     | 200 OK 

## API Details

### Create a Product
- **URL:** `/products`
- **Method:** `POST`
- **Description:** This endpoint allows you to create a new product by sending a JSON request body with the product details such as name, description, price, and quantity.
- **Request Body (JSON):**
  ```json
  {
    "name": "Product Name",
    "description": "Product Description",
    "price": 19.99,
    "quantity": 100
  }
  ```
- **Response:**
  - 201 Created: The product is successfully created.
  - 400 Bad Request: Invalid request body.

### Read a Product
- **URL:** `/products/{product_id}`
- **Method:** `GET`
- **Description:** This endpoint allows you to retrieve the details of a specific product by providing its `product_id` in the URL.
- **Response:**
  - 200 OK: The product details are returned in the response body.
  - 404 Not Found: Product not found.

### Update a Product
- **URL:** `/products/{product_id}`
- **Method:** `PUT`
- **Description:** This endpoint allows you to update an existing product by providing its `product_id` in the URL and sending a JSON request body with the updated product details.
- **Request Body (JSON):**
  ```json
  {
    "name": "New Product Name",
    "description": "New Product Description",
    "price": 24.99,
    "quantity": 75
  }
  ```
- **Response:**
  - 200 OK: The product is successfully updated.
  - 400 Bad Request: Invalid request body.
  - 404 Not Found: Product not found.

### Delete a Product
- **URL:** `/products/{product_id}`
- **Method:** `DELETE`
- **Description:** This endpoint allows you to delete a product by providing its `product_id` in the URL.
- **Response:**
  - 204 No Content: The product is successfully deleted.
  - 404 Not Found: Product not found.

### List All Products
- **URL:** `/products`
- **Method:** `GET`
- **Description:** This endpoint allows you to retrieve a list of all products in the system.
- **Response:**
  - 200 OK: An array of product objects is returned in the response body.

## Project File Structure
- This API is organized using the following file structure:
  ```
  ├── api/
  │   ├── __init__.py
  │   ├── models.py
  │   ├── views.py
  └── manage.py
  ```

## requirements:

- flask
- tinydb
