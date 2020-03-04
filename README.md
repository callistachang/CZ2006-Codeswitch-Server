# CodeSwitch Server

Built with Django REST Framework 0.1.0, to be deployed on Heroku.

## How to Run Locally

On the terminal, go to the root directory and install dependencies first if you haven't:

```
pip install -r requirements.txt
```

Then, run the server on `http://127.0.0.1/8000/`:

```
python manage.py runserver
```

You can use Postman to send API requests to the endpoints. You can check out `http://127.0.0.1/8000/` on the browser to check out which API endpoints are done so far.

To access our admin site, go to `http://127.0.0.1/8000/admin/` and enter the secret email and password.

## Misc Notes

If code changes are made to the models, you must migrate the changes. Navigate to the root directory, then do the following:

```
python manage.py makemigrations
python manage.py migrate
```