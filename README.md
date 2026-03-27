# Sticky Notes (Django)

A simple sticky-notes web app: register, log in, create/edit/delete notes, choose colors, pin notes, search, and browse with pagination.

## Requirements

- Python 3.10+
- pip

## Setup

1. **Create and activate a virtual environment (recommended)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

4. **Run the development server**

   ```bash
   python manage.py runserver
   ```

5. **Open the app**

   In your browser go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (root redirects to the notes list; you may be asked to log in).

## Optional: create an admin user

```bash
python manage.py createsuperuser
```

Then visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Features

- **Pagination:** The note list shows **10 notes per page** (see `NOTES_PER_PAGE` in `notes/views.py`).
- **Character counter:** On the create/edit note form, the content field shows a live character count (updated with JavaScript).

## Project layout

- `manage.py` — Django entry point
- `sticky_project/` — project settings and URLs
- `notes/` — notes app (models, views, forms, templates, static assets)
