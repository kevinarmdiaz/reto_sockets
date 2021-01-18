# Reto sockets

Reto sobre sockets donde se simulará un dispositivo que reporta variables como temperatura y keep_alive, un servidor que reciba las datos de ese dispositivo y un backend en django para reportar los datos

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Instalar docker en tu máquina local_

### Instalación 🔧

_Con docker instalado..._

_Crearemos las imagenes de cada proyecto, el cual esta dividido en 3 carpetas_
### DOCKER_SERVER
_Para crear la imagen de este proyecto, ejecutaremos los siguientes comandos en el directorio del proyecto_

```
$ docker build -t server_image .
```

_Con el comando ejecutado, construiremos la imagen. Ahora queda comprobar que existe la imagen_

```
$ docker images
```

|REPOSITORY|   TAG |     IMAGE ID  |     CREATED|       SIZE|
| --- | --- | --- |--- | --- |
|server_image| latest |  70a92e92f3b5|   1 hour ago |  991MB|

_Copiaremos el nombre de la imagen y ejecutaremos el comando para iniciar la imagen_

```
$docker run -it -p 8889:8889 server_image
```
_Como observamos la imagen estará corriendo y el servidor está listo para aceptar peticiones_

### DOCKER_BACKEND

_Para crear la imagen de este proyecto, ejecutaremos los siguientes comandos en el directorio del proyecto_

```
$ docker-compose build
$ docker-compose run web /usr/local/bin/python manage.py migrate
$ docker-compose up

```
_Ahora el proyecto estará corriendo en el puerto 8000 en localhost_

_Se deberá crear un dispositivo nuevo para realizar las pruebas, para ello dirigirse a la ruta:_

_http://localhost:8000/api/devices/create/_

_Dar clic en POST_
```
{
    "id": 1,
    "created_at": "2021-01-16T09:33:22.934305-05:00",
    "updated_at": "2021-01-16T09:33:22.934366-05:00",
    "name": "test Full",
    "last_temperature": 60.0,
    "keep_alive": "2021-01-16T09:33:00-05:00",
    "threshold_temperature": 30.0
}
```
_El dispositivo, estará creado_

### DOCKER_DEVICE

_Para crear la imagen de este proyecto, ejecutaremos los siguientes comandos en el directorio del proyecto_

```
$ docker build -t device_image .
```

_Con el comando ejecutado, construiremos la imagen. Ahora queda comprobar que existe la imagen_

```
$ docker images
```

|REPOSITORY|   TAG |     IMAGE ID  |     CREATED|       SIZE|
| --- | --- | --- |--- | --- |
|device_image| latest |  40a92ef3b5|   1 hour ago |  300MB|

_Copiaremos el nombre de la imagen y ejecutaremos el comando para iniciar la imagen_

```
docker run device_image
```
_Como observamos la imagen del dispostivo estará corriendo y estará enviando datos al servidor sockets_



## Ejecutando las pruebas ⚙️

_Verificar la consola de los 3 proyectos para verificar su correcta ejecución_




## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Tornado](https://www.tornadoweb.org/en/stable/) - 
* [Django](https://www.djangoproject.com/) - 




---
