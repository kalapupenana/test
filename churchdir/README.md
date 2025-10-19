# Church Directory (Django)

A minimal Django app for branch ministers to log in and edit only their branch members.

## Quick start (local)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser  # your admin

# optional: seed branches
python seed_branches.py

python manage.py runserver
```

Login at: http://127.0.0.1:8000/admin/

## Docker (prod-ish)

```bash
docker build -t churchdir .
docker run -p 8000:8000 --env DJANGO_SETTINGS_MODULE=churchdir.settings churchdir
```

## Seed branches & example minister

```bash
python seed_branches.py
```

## CSV Import (Admin > Members > Import)

Columns must be: `Hingoa,Fakaiku,Aho Fa'ele'i,T/F,Kolo,Status`.

## Notes
- Default DB is SQLite. You can later switch to Postgres.
- Per-branch permissions are enforced in `core/admin.py`.
