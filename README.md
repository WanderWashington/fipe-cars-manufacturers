# Fipe cars and manufacturers
Developed in Django and Django Rest Framework, this project contains a API to get a Cars and Manufacturers, based in FIPE. Have a two routes:

    /veiculo/    
    /marca/    

# Endpoints

Search in manufacturer by `code`, not pk:

    /marca/?code={code}

Search in the cars, by manufacturer `pk` :

    /veiculo/?manufacturer={pk}


