=========
fipe_api
=========

Developed in Django and Django Rest Framework, 
this app contains a API to get a Cars and Manufacturers, based in FIPE.


Quick start
-----------

1. Add "fipe_api" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'fipe_api',
    ]

2. Include the fipe_api URLconf in your project urls.py like this::

    path('fipe_api/v1/', include('fipe_api.urls')),

3. Run `python manage.py migrate` to create the fipe_api models.

4. Run `python manage.py loaddata fixtures/fipe_api.json`

5. Start the development server and visit http://127.0.0.1:8000/fipe_api/v1/
   to access the api routes.

Endpoints
-----------

`fipe_api/v1/veiculo/`
`fipe_api/v1/marca/`

Search Parameter
----------------
To search by code in manufacturer add `?code=` in the route and type the code number that want search:

/marca/?code={code}

To search by manufacturer in the cars, add `?manufacturer=` in the route and type a manufacturer `pk` that want search:

/veiculo/?manufacturer={pk}

Extra commands
---------------

Load the json with name `marcas.json`:

python manage.py get_data

Get cars data from the website, using selenium to get data and save in database using Django methods:

python manage.py scrap_data_selenium