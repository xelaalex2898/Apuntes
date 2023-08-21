#Active Direcory

¿Que es un directorio?
--
un directorio es una estructura jerarquica que almacena información sobre los objetos en la red 
Un servicio como AD proporciona los métodos y herramientas para guardar infomarción de manera jerarquica y poner a disposición esta información a los usuarios y administradores de la red 

###### consultar datos de directorio
¿Que es un dominio?
    En el contexto de los sistemas operativos Windows, un dominio es un conjunto de recursos de red, como usuarios, grupos, equipos y recursos compartidos, que están organizados y administrados de manera centralizada. Un dominio proporciona un mecanismo de seguridad que controla el acceso a estos recursos y simplifica la administración de la red.

    En un dominio de Windows, todos los recursos de red son administrados por un controlador de dominio, que es un servidor que ejecuta el servicio de Active Directory. Los usuarios y los equipos se agregan al dominio y se autentican en el controlador de dominio para acceder a los recursos de la red.

    El controlador de dominio mantiene una base de datos centralizada, llamada base de datos de Active Directory
    * esto es igual que en SO, la análogía es: * 
    los recursos de una computadora son los recursos de un domino y el SO que los administra es el controlador


Seguridad
--
La seguridad se integra con active directory mediante la autenticación con inicio de sesión y control de acceso alos objetos del directorio

Esto hace la tarea de los administradores mucho más sencilla incluso en las redes más complejas

###### consultar introducción a la seguridad

¿Que incluye AD?
--

+ un conjutno de reglas
    es el esquema que define los objetos del directorio, las restricciones y limites de las instancias de estos objetos y el formato de sus nombres
###### consultar esquema 

+ un catalogo global 
    que contiene información acerca de todos los objetod del directorio, esto es independiente del dominio donde se encuentre el usuario o el recurso 
+ un mecanismo de consulta e indice
    para poder publicar los objetos y sus propiedades y poder buscar por usuarios y aplicaciones de red
##### ¿¿¿¡¡¡!!!???
+ Un servicio de replicación de datos
    Todos los controladores de dominio de un dominio contienen una copia de del directorio
    Esto garantiza que todos los controladores de dominio tengan una copia completa y actualizada de la información de directorio, lo que permite a los usuarios acceder a los recursos de red de manera eficiente y sin interrupciones.

    La replicación de Active Directory es útil porque proporciona redundancia y resiliencia en caso de fallos de hardware o software en un controlador de dominio. Si un controlador de dominio falla, los usuarios pueden seguir accediendo a los recursos de la red a través de otros controladores de dominio que contienen una copia actualizada de la información de directorio.


# Autenticación vs autprización 

    la autenticación es la demostración de que eres quien dices ser, mientras que existen casos donde puede ocurrir que aunque estés autenticado no tengas permiso para llevar a cabo algúna actividad o acceder a un servicio, acceder a ciertos datos, etc. 

    Esto tiene la ventaja de seguridad, ya que reduce el área de ataque. 
    Todas estas tareas se le delegan a active directory



