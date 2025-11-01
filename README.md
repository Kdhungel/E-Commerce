# Django E-Commerce Project

This is a **learning project** where I’m building a full-featured E-Commerce website step by step.

## What is inside

- Setting up Django project & apps
- Templates, static files, and Bootstrap integration
- Models for Products, Categories, Cart, Orders
- User authentication (custom user model)
- Cart functionality (add, remove, increment, decrement)
- Orders and payments (PayPal integration)
- Product variations, ratings, and reviews
- Using Git & GitHub for version control

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Kdhungel/E-Commerce.git
   cd E-Commerce
2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the server:

   ```bash
   python manage.py runserver
   ```

6. Open in browser:

   ```
   http://127.0.0.1:8000/
   ```

## Notes

* Static files are in the `static/` folder.
* Media files (images, banners, avatars) are served from `static/images/`.
* This project is for **learning and practice purposes**.

