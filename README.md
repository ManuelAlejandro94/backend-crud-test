# Crud Backend Test

## Estructura

```
backend-crud-test
│   README.md
│   requirements.txt
│   config.yml
│
└───src
│   │
│   └───crud
│       │   __init__.py
│       │   scouts.py
│       │   version.py
│       └───web
│           │   __init__.py
│           │   __main__.py
│           │   wsgi.py
│           └───services
│               │    __init__.py
│               │    delete_client.py
│               │    get_clients.py
│               │    new_client.py
│               │    update_client.py
│   
└───static
└───templates
```

## Configuración

Versión de python utilizada: 3.8
Versión de pip utilizada: 22.2.2

* Colocarse dentro del directorio `backend-crud-test`
* Usando consola del SO de preferencia crear nuevo entorno virtual:
```
$ virtualenv <env_name>
```
* Activar entorno virtual
```
$ source <env_name>/bin/activate
```
* Con el entorno virtual activo instalar paquetes requeridos
```
(<env_name>)$ pip install -r requirements.txt
```
En caso de encontrarse a través de un proxy:
```
(<env_name>)$pip install --proxy http://<usr_name>:<password>@<proxyserver_name>:<port#> -r requirements.txt
```
* Editar `config.yml` con los datos de la BD de mongo

_**NOTA:** La base de datos utilizada es mongo, con una única colección. El id de los datos proporcionados, está en bd como \_id_ 

## Despliegue de la aplicación

### Consola
Teniendo el entorno virtual activo y encontradose dentro de `backend-crud-test` usando la configuración por defecto:
```
python -m src.crud.web.__main__
```
En caso de necesitar desplegar por otro puerto o utilizar otro archivo de configuración se puede utilizar:
```
python -m src.crud.web.__main__ -p <port> -c <config.yml>
```

### Usando IDE PyCharm

![Employee data](static/Config_PyCharm.png?raw=true "Config PyCharm")
 Después de crear esa configuración dar click a botón de Run

## Debuggear aplicación

Repetir los pasos de `Usando IDE PyCharm` solo que utilizar el botón de Debug en esta ocasión

## Probando aplicación
Se incluye colección con todos los path del aplicativo para ser probado en postman. Se puede encontrar en `static/backend-crud-test.postman_collection.json`

## Que no incluye el aplicativo
* Manejo de excepciones para devolver una respuesta controlada en cada path.
* Comprobación de parámetros recibidos (longitudes, tipo de dato, etc)
* Códigos de error específicos en las respuestas que tienen algún error.
* Protocolos de autenticación como OAuth2

## Que no incluye la base de datos
* Uso de procedimientos almacenados
* Catálogo de status

## MySql
El dump de la BD utilizada se encuentra en `static/mysql/crud_test_db_clients.sql`

##Endpoints
El aplicativo cuenta con solo 4 endpoints.

```
  GET     /clients
  POST    /clients
  PUT     /clients/:id
  DELETE  /clientes/delete/:id
```
Los únicos endpoints que necesitan recibir información en el cuerpo de la petición son:
* POST
* PUT

### Ejemplos

#### POST /clients
```
{
    "firstName": "ALEJANDRO",
    "lastName": "ALVAREZ",
    "phone": "2292235259",
    "email": "manuel_ale94@outlook.com",
    "age": 28,
    "status": "Nuevo"
}
```

#### PUT /clients/:id
```
{
    "firstName": "ALEJANDRO",
    "lastName": "ALVAREZ",
    "phone": "2292235259",
    "email": "manuel_ale94@outlook.com",
    "age": 28,
    "status": "Nuevo"
}
```