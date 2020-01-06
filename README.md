# Fipe cars and manufacturers
Developed in Django and Django Rest Framework, this project contains a API to get a Cars and Manufacturers, based in FIPE. Have a two routes:

    /veiculo/    
    /marca/    

# Search parameter

To search by code in manufacturer add `?code=` in the route and type the code number that want search:

    /marca/?code={code}

To search by manufacturer in the cars, add  `?manufacturer=` in the route and type a manufacturer pk that want search:

    /veiculo/?manufacturer={pk}


