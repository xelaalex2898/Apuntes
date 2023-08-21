#Curso API REST


¿Que es una API?
--
    Una API es un servicio web cunsumible por el cleinte.
    sus siglas son Application Programming Interface. 
    Son conjuntos de herramienta y estandares que los desarrolladores usamos para hacer que varios servicios o sistemas se comuniquen entre sí.
    Las API´s son muy útiles porque pueden hacer que varios programas se comuniquen incluso sin ser del mismo lenguaje o mismo framework o no tener nada en común más que la capacidad de lectura y modificación de ciertos tipos de archivos. 
¿Que es REST?
--
    REST es un tipo de arquitectura muy usada en todo el mundo que se utiliza principalmente en servicios WEB.
    Los sistemas REST-full utilizan estandares HTTP con operaciones o verbos del tipo 
    
    PUT
    POST 
    GET 
    DELETE
    PATCH
    
    Que son formas de manejar recursos del lado del servidor.

¿Que es un recurso?
--

    Us recurso es una entidad que se puede ser accedida y manipulada por una URL (Uniform Resourse Locator) y la representación de los datos obtenidos por el recurso pueden ser representados en forrmatos XML, JASON o HTML;

¿Que es un servidor?
--

    En terminos generales los servidores son software o hardware que provee recursos o servicios a otros programas o dispositivos llamador clientes, que están interconectados a traves de una red. 
    Estos pueden ser de diferentes tipos, como servidores web, servidores de bases de datos, servidores de archivos, servidores de correo electrónico, entre otros. 


Mensajes del lado del servidor
--

    El servidor regresa valores al cliente sobre su petición en distintos casos, en casos de exito, cuando se devolvió correctamente el recurso solicitado. 

    Sus tipos son:

    Exito(2xx) indican que la solicitud se ha procesado correctamente
    
    Redirecciones (3xx) Indican que el recurso solicitado se ha cambiado de lugar  y se debe redirigir al cliente a la nueva ubicación.

    Errores del cliente (4xx) indican que ha habido un error del lado del cliente como una solicitud mal formada o falta de conexión  internet.

    Errores del servidor (5xx) Indican que ha habido un error del lado del servidor al procesar la solicitud como un servidor caído o una base de datos inaccesible



## Análisis del template para apis de .NET

MVC (Model View Controller)
--

El sistema arquitectónico del template de web api no usa la marte de views, así que es un MC model controller ó ApiController

Carpetas y archivos del template
--

dir controller:

    es donde se ponen todas las clases que contienen los controladores o la lógic que maneja los modelos.
    Para los  archivos dentro de este directorio deben contener la palabra "Controller" al final del nombre, al igual que las clases, que deben heredar de ControllerBase

###### Sintxis:

    Public class dirnameController : ControllerBase
    {
        content 
    }

Midelwers
--

Es una serie de instrucciones de código que se realizan entre la petición del usuario y la respuesta del servidor a lo largo del tiempo de vida de la ejecución de peticiones http

un middleware actúa como un intermediario entre una solicitud de un cliente y el servidor que procesa esa solicitud. El middleware se utiliza para realizar tareas comunes que se aplican a todas las solicitudes, como la autenticación, la autorización, el registro, la compresión de contenido y la gestión de errores.

Los midelwares se agregan en una secuencia llamada pipeline, el orden de esta pipeline es muy importante 

* El middleware de logging: Este middleware registra información sobre la solicitud y la respuesta, como la hora en que se recibió la solicitud, la URL solicitada y el código de estado de la respuesta.

* El middleware de excepciones: Este middleware maneja cualquier excepción que se produzca durante la ejecución de los middlewares o la aplicación, y devuelve una respuesta de error adecuada al cliente.

* El middleware de redireccionamiento: Este middleware se encarga de redirigir el tráfico de la solicitud a otra URL o ruta, si es necesario.

* El middleware de enrutamiento: Este middleware se encarga de enrutamiento de la solicitud a la ruta correspondiente en la aplicación.

* El middleware de autenticación: Este middleware se encarga de la autenticación del usuario y establece el contexto de seguridad para la solicitud.

* El middleware de autorización: Este middleware se encarga de verificar si el usuario tiene los permisos necesarios para acceder a la ruta o recursos solicitados.

Los middlewares personalizados: Aquí es donde se ejecutan los middlewares personalizados que han sido agregados por el desarrollador para realizar tareas específicas en la aplicación.

* El middleware de la aplicación: Este middleware se encarga de ejecutar la aplicación real y generar la respuesta.