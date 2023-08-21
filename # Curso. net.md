# Curso. net

## Historia de .net
 .net es una versión de un framework que solo corria en widows llegó hasta la versión 4.8 en 2016 microsoft tomó la decisión de crear un nueco framework que fuese multiplataforma. Así se creó .net core que empieza en su versión 5

## ASP .NET CORE 
es un framework que sirve para programar páginas web y es multiplataforma, funciona en windows, linux y mac os
sus siglas significan Active Server Pages. 
Viene con muchas herrramientas útiles para crear páginas web
como 
* sistema de ruteo 
* distema de usuarios
* inyección de dependencias
* entre muchas otras

Una de sus ventajas es la velocidad, cada que se actualiza el framework mejora su velocidad, así que sin cambiar el código puedes optener una página mucho más rápida

## ASP .NET CORE MVC

### explorando el proyecto

Una solución es la combinacion de varios proyectos. así podemos decidir tener muchos proyectos en una misma solucion 
Debajo de la solucion aparecen nuestros proyectos, si hacemos click en el proyecto se abre un archivo .csproj que tiene la configuración central del proyecto, como por ejemplo la versión del framework  y las dependencias implicitas. 

### Dependencias. 

en dependencias podemos agregar librerias y así poder usar sus servicios de manera sencilla. 

### propterties

en esta carpeta hay un archivo launchsetting.json 
en este archivo podemos ver los distintos perfiles , las variables de entorno, el tipo de ambiente como de desarrollo o producción.
 
### wwwrooot. 

en esta carpeta se incluyen los archivos estáticos de nuestra aplicación.

### controllers 

los controladores son las clases que reciven las petociones http de los usuarios, las procesan y envian una respuesta, en el caso de mvc esta respuesta es una vista, pero puedo no ser así. 

### modelos. 

los modelos son los bloques que administran los datos, sus relaciones operaciones con ellos etc. 

### views 

en esta carpeta se coloca todo el contenido visual de la app

### appsetting.json 

estos nos permiten guardar la configuracion  de nuestro poryecto. 
appsetings.json se usa en produccion y appsettings.develoment.json en desarrollo. estos se relacionan con el archivo .csproj

## controllers 

los controllers pueden tener una o más acciones, las acciones son métodos con 
	IActionresult name
	{
		return view();
	{

## Rooteo:



##JWT Api REST
## Data Models
Para crear modelos de base de datos de manera rápida debemos dar click derecho en la solución, luego dar click en EF Core Power tools, reverse engenier y  seguir el proceso. 
Esto genera una carpeta models con todos los modelos relacionados y agrega la base de datos al contexto. 

Aún debemos crear un "conection string"
Para ello debemos editar el archivo appsettigs.json y agregar una nueva llave que se llame "ConnectionStrings" y para agregar su valor 
vamos a view en la pestañas de VS y abrimos el explorador de objetos sql, si no tienes el servidor registrado se puede agregar arriba de esta pestaña, seleccionamos el servidor, damos click derecho en la base de datos y luego en propiedades, por último buscamos el campo que se llame conection string o cadena de conexion 
Luego debemos crear el servicio para ello tenemos la opción de crearlo a mano o podemos dar click derecho en la carpeta controladores y agregar, nuevo controlador, api, api controller with actions using entity framwork
 	 















