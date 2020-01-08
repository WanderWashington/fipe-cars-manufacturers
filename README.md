# Fipe cars and manufacturers
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

Developed in Django and Django Rest Framework, this project contains a API to get a Cars and Manufacturers, based in FIPE.

## Installation:
1.  Install the requirements file, with the command:

    ```pip install -r requirements.txt```

2.  Create your database and configure it in the `settings.py`  file.

2.  Load the migrations with the command:

    ```python manage.py migrate```

3.  Load the fixtures with the cars and manufacturers data:

    ```python manage.py loaddata fipe_api.json```

### Endpoints:

    /veiculo/    
    /marca/    

### Search parameter:

To search by code in manufacturer add `?code=` in the route and type the `code` number that want search:

    /marca/?code={code}

To search by manufacturer in the cars, add  `?manufacturer=` in the route and type a manufacturer `pk` that want search:

    /veiculo/?manufacturer={pk}

### Extra commands:

Load the json with name `marcas.json`:

```python manage.py get_data```

    
Get cars data from the website, using selenium to get data and save in database using Django methods:

```python manage.py scrap_data_selenium```
