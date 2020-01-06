# Fipe cars and manufacturers



Developed in Django and Django Rest Framework, this project contains a API to get a Cars and Manufacturers, based in FIPE. Have a two routes:

    /veiculo/    
    /marca/    

# Search parameter

To search by code in manufacturer add `?code=` in the route and type the `code` number that want search:

    /marca/?code={code}

To search by manufacturer in the cars, add  `?manufacturer=` in the route and type a manufacturer `pk` that want search:

    /veiculo/?manufacturer={pk}

# Installation
1.  Install the requirements file, with the command:

    ```pip install -r requirements.txt```

2.  Create your database and configure it in the `settings.py`  file.

2.  Load the migrations with the command:

    ```python manage.py migrate```

3.  Load the fixtures with the cars and manufactures data:

    ```python manage.py loaddata data.json```

# Extra commands:

Load the json with name `marcas.json`:

```python manage.py get_data```

    
Get cars data from the website, using selenium to get data and save in database using Django methods:

```python manage.py scrap_data_selenium```
