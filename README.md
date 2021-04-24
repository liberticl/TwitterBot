# Twitter Bot
Un bot para dar like y retweet a las cuentas que desees! Además, sigue a las cuentas mencionadas en los RT que realices.

***Importante**: sólo ha sido probado en Ubuntu 18.04 (servidor y escritorio), utilizando Python 3.*

## Instalación
Las librerías de que depende este código se encuentran en `requirements.txt`. 

Para crear el entorno virtual en el directorio actual se debe ejecutar el siguiente comando:

    python3 -m venv .
    
Para ingresar al entorno virtual, se debe ejecutar:

    source bin/activate

Finalmente, para instalar dependencias:

    pip3 install -r requirements.txt

## Preparación
Antes de poder ejecutar el programa se deben obtener las credenciales de acceso a la API de Twitter y establecer los usuarios en los que se fijará el programa.

### API Twitter
1. Ingresa al sitio de desarrolladores de Twitter para [crear una nueva app](https://developer.twitter.com/en/portal/apps/new) (el sitio está en inglés) utilizando tu usuario de Twitter.
2. Ingresa un nombre a la aplicación y selecciona _Complete_. 
3. Guarda los valores de _API Key_ y _API Secret Ket_. Finalmente haz click para ir a _App settings_.
4. Edita los permisos de la aplicación (inicialmente sólo permite lectura), indicando _Read and Write_.
5. Busca el apartado _Keys and tokens_, y una vez dentro de este, busca _Access Token and Secret_. Haz click sobre el botón _Generate_ al costado derecho y guarda los dos valores que aparecerán en pantalla.

### Archivo para API
Debes crear un archivo llamado `.api_data.yml` (en linux, este es un archivo oculto). Puedes utilizar el nombre que desees, pero para que sea válido, debes indicar el nombre de archivo que utilices en la función `get_credentials()` de `tools.py`.

En el archivo debes escribir lo siguiente:

    consumer_key: CONSUMER_KEY
    consumer_secret: CONSUMER_SECRET
    access_token_key: ACCESS_TOKEN_KEY
    access_token_secret: ACCESS_TOKEN_SECRET

cambiando los elementos que están en mayúscula por los valores guardados previamente.

### Usuarios
Para que el programa realice acciones con los usuarios, debes crear una carpeta llamada `db` y en su interior, crear un archivo sin extensión con el nombre de usuario que se desea agregar al listado. En su interior, el único dato que se debe ingresar es el ID del último tweet realizado por este usuario.

Por ejemplo, el nombre de mi usuario en Twitter es [*fco_vergara12*](https://twitter.com/fco_vergara12), por lo tanto, al ingresar en mi perfil, el último post que realicé será el primero (no fijado y no retwitteado) que aparezca. En el navegador, este tweet tiene el link

https&#58;/twitter.com/fco_vergara12/status/XXXXXXXXXXXXXXXXXXX

El número representado por _XXXXXXXXXXXXXXXXXXX_ corresponde al ID del tweet, por lo tanto, es este número el único elemento que contendrá el archivo llamado `fco_vergara12`.

### Ejecución
En la terminal, aún dentro del entorno virtual, se debe ejecutar:

    python3 main.py

Para salir del entorno virual, basta:

    deactivate


## A considerar

### Límites
La API de Twitter mantiene limitadas las distintas funcionalidades a una cierta cantidad por cada cierto lapso de tiempo. Estos límites se encuentran [**aquí**](https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits).

En particular, esta implementación se recomienda ejecutar **cada 15 minutos o más**.

### Automatización
Esta implementación está diseñada para funcionar una vez, sin embargo, está pensada para elevat la actividad de un usuario de Twitter que da poco uso a la plataforma (o cualquier motivo similar).

Por lo mismo, es preferible mantener una tarea de _crontab_ ejecutando este programa cada cierta cantidad de tiempo, para esto, se debe abrir el editor con `crontab -e` y agregar una línea de código similar a:

    */XX * * * * PYENV_PATH PATH/main.py > LOG_PATH 2>&1

Donde: 

- XX corresponde a la cantidad de miutos entre una ejecución y la próxima.
- PYENV_PATH es la ruta completa del entorno, por ejemplo */home/user/Twitter/bin/python3*
- PATH es la ruta completa hasta el directorio donde se encuentra `main.py`, por ejemplo */home/user/Twitter/*
- LOG_PATH es la ruta completa hasta dónde deseamos que se encuentre el archivo `.log` del programa (aquí se imprime el resultado del código o errores en su última ejecución). Un ejemplo puede ser */home/user/Twitter/twitter.log*

**Importante**: con esto, lo único que se debe hacer desde ahora en adelante es [agregar usuarios](#Usuarios) o eliminarlos (basta borrar el archivo correspondiente al usuario que se desea sacar del listado).