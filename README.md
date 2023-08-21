
## Run Locally

Clone the project

```bash
  git clone https://github.com/davisonv/base-erp-backend
```

Go to the project directory

```bash
  cd my-project
```

Create a venv

```bash
  python -m venv venv
```

Activate the venv

```bash
  source ./venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Make the migrations then migrate

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Run the development server

```bash
  python manage.py runserver
```
