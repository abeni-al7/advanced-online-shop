# Advanced Online Shop

This project is an advanced online shop built with Django, Celery, Redis, and Stripe. It includes features such as product listings, shopping cart, order management, payment processing, recommendations, and internationalization.

## Features

-   **Product Catalog:** Browse products by category.
-   **Shopping Cart:** Add, remove, and update items in the cart.
-   **Order Management:** Create and manage orders.
-   **Payment Processing:** Secure payment processing with Stripe.
-   **Product Recommendations:** Recommendation engine based on purchase history.
-   **Coupons:** Apply coupons for discounts.
-   **Internationalization:** Support for multiple languages (English and Spanish).
-   **Asynchronous Tasks:** Utilizes Celery for asynchronous tasks such as sending order confirmation emails.
-   **Admin Interface:** Django admin interface for managing products, categories, orders, and coupons.

## Technologies Used

-   **Django:** Web framework
-   **Celery:** Asynchronous task queue
-   **Redis:** In-memory data store for the recommendation engine
-   **Stripe:** Payment gateway
-   **WeasyPrint:** PDF generation
-   **django-parler:** For providing translations of models
-   **localflavor:** For local flavor form fields and validators
-   **django-rosetta:** Translation tool

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/abeni-al7/advanced-online-shop
    cd advanced-online-shop
    ```

2.  **Create a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**

    -   Create a [.env](http://_vscodecontentref_/0) file based on [.env.example](http://_vscodecontentref_/1) and fill in the required values:

        ```
        STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
        STRIPE_SECRET_KEY=your_stripe_secret_key
        STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
        ```

5.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Collect static files:**

    ```bash
    python manage.py collectstatic
    ```

8.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

9.  **Run Celery worker:**

    ```bash
    celery -A myshop worker -l info
    ```

10. **Run Flower for monitoring Celery (optional):**

    ```bash
    celery -A myshop flower
    ```

## Configuration

-   **Django settings:** Configure the [settings.py](http://_vscodecontentref_/2) file for database settings, internationalization, and other settings.
-   **Stripe:** Set up your Stripe account and configure the API keys and webhook secret in the [.env](http://_vscodecontentref_/3) file.
-   **Redis:** Ensure Redis is running and configure the connection settings in [settings.py](http://_vscodecontentref_/4).
-   **Celery:** Configure Celery settings in [celery.py](http://_vscodecontentref_/5) and [settings.py](http://_vscodecontentref_/6).

## Usage

1.  **Access the admin interface:**

    -   Go to `/admin/` in your browser and log in with the superuser credentials.

2.  **Manage products and categories:**

    -   Use the admin interface to create and manage product categories and products.

3.  **Place orders:**

    -   Browse the product catalog and add products to your cart.
    -   Proceed to checkout and fill in the order form.
    -   Complete the payment process using Stripe.

4.  **Apply coupons:**

    -   Enter a valid coupon code in the cart to apply a discount.

5.  **View order details:**

    -   Order details can be viewed in the admin interface.

## Internationalization

-   The project supports English and Spanish.
-   To translate the project, use [django-rosetta](http://_vscodecontentref_/7).
-   Install [django-rosetta](http://_vscodecontentref_/8) using pip.
    ```
    pip install django-rosetta
    ```
-   Add `rosetta` to the installed apps in [settings.py](http://_vscodecontentref_/9).
-   Add [path('rosetta/', include('rosetta.urls'))](http://_vscodecontentref_/10) to [urls.py](http://_vscodecontentref_/11).
-   Translate the strings using the rosetta UI.
-   Run `python [manage.py](http://_vscodecontentref_/12) compilemessages` to compile the translations.

## Project Structure

. ├── cart/ # Shopping cart app ├── coupons/ # Coupon management app ├── locale/ # Translation files ├── myshop/ # Main project directory ├── orders/ # Order management app ├── payment/ # Payment processing app ├── shop/ # Shop app (products, categories) ├── static/ # Static files (CSS, images) ├── .env # Environment variables ├── manage.py # Django management script ├── requirements.txt # Project dependencies └── README.md # Project documentation

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Submit a pull request.


