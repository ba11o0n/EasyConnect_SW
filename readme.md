## File Hireachy Explanation :

### `core/` – The Project Configuration Folder

This is the  **main project folder** created by:

```bash
django-admin startproject core .
```

It holds the global settings and configuration for your Django site.

**Files inside `core/`:**

* `__init__.py`: Makes this folder a Python package.
* `settings.py`: **The brain of your project.** Here you configure:

  * Installed apps
  * Database
  * Middleware
  * Templates
  * Static files, etc.
* `urls.py`: The **global URL dispatcher**. You include app routes here.
* `wsgi.py` & `asgi.py`: For deployment. Used by web servers to run Django apps.

---

### `main/` – Main Application Logic

This is where the **site’s main features** live (e.g. home page, dashboard, etc.).

Created by:

```bash
python manage.py startapp mainapp
```

**Files inside `main/`:**

* `models.py`: Define your database models here.
* `views.py`: Define the logic behind your web pages (controllers).
* `urls.py`: Add URL patterns specific to `mainapp` (you create this).
* `templates/` (optional): Holds HTML templates for this app.
* `admin.py`: Register your models to Django admin.
* `apps.py`: Configuration class for this app.
* `tests.py`: Write tests here (optional but recommended).
* `migrations/`: Tracks database changes.

---

### `auth/` – Handles Authentication

This app is **dedicated to login, logout, registration, password reset**, etc.
It separates user management from your main app logic.

Created by:

```bash
python manage.py startapp authapp
```

**Structure is just like `mainapp`**, but focused on user accounts:

* `models.py`: You could define a custom `User` model or `Profile`.
* `views.py`: Functions like `login_view()`, `logout_view()`, etc.
* `urls.py`: Routes like `/auth/login/`, `/auth/register/`, etc.
* `forms.py` (optional): Define custom registration/login forms here.
