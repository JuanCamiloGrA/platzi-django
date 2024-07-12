# Django Project

.env/
.gitignore
.pytest_cache/
README.md
.vscode/
accounts/
core/
db.sqlite3
manage.py
media/
orders/
products/
requirements.txt
templates/


### Key Directories and Files

- **accounts/**: Contains the accounts application, including models, views, and templates.
- **core/**: Contains the core settings and configurations for the Django project.
- **orders/**: Contains the orders application, including models, views, and templates.
- **products/**: Contains the products application, including models, views, and templates.
- **manage.py**: Django's command-line utility for administrative tasks.
- **requirements.txt**: Lists the dependencies required for the project.
- **templates/**: Contains shared HTML templates.

## Setup

### Prerequisites

- Python 3.x
- Django 5.0.6
- Virtualenv

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Set up environment variables:
    - Create a `.env` file in the `core/` directory with the appropiate content.
    ```
    SECRET_KEY=<your-secret-key>
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ...
    ```

6. Apply migrations:
    ```sh
    python manage.py migrate
    ```

7. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Applications

### Accounts

- **Models**: [accounts/models.py](accounts/models.py)
- **Views**: [accounts/views.py](accounts/views.py)
- **Admin**: [accounts/admin.py](accounts/admin.py)
- **URLs**: [accounts/urls.py](accounts/urls.py)

### Orders

- **Models**: [orders/models.py](orders/models.py)
- **Views**: [orders/views.py](orders/views.py)
- **Admin**: [orders/admin.py](orders/admin.py)
- **URLs**: [orders/urls.py](orders/urls.py)
- **Forms**: [orders/forms.py](orders/forms.py)

### Products

- **Models**: [products/models.py](products/models.py)
- **Views**: [products/views.py](products/views.py)
- **Admin**: [products/admin.py](products/admin.py)
- **URLs**: [products/urls.py](products/urls.py)

## Configuration

### Settings

- **INSTALLED_APPS**: Defined in [core/settings.py](core/settings.py)
- **ROOT_URLCONF**: Defined in [core/settings.py](core/settings.py)

## Running Tests

To run tests, use the following command:
```sh
python manage.py test
```

## License

This project is licensed under the MIT License.