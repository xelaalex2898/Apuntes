

# ¿Que es C#?
C# es la solución de microsoft para la creación de software. Sobre todo sobre el framesork .NET

Tipos de datos primitivos
-----
Existen tres tipos de datos primitivos, los enteros, reales y booleanos

* bool: Verdadero y falso 
* byte: numéricos de 8 bits con signo
* ubyte: numéricos de 8 bits con signo
* short: numéricos de 16 bits con signo
* int: numéricos de 32 bits con signo
* uint: numéricos de 32 bits sin signo
* float: numéricos de 64 bits con signo
* double: punto flotante de 64 bits con signo
* decimal:Precisión fija de 128 bits
* char: un solo caracter de 16 bits
* string: cadenas de caracteres cantidad de memoria indefinida

##### Enteros
###### con signo 
Porque tienen signo positivo. 
     sbyte
     short
     int 
     long

###### sin signo 
porque hacen distinción de signo

    float
    double 
    decimal


Tipos de datos de referencia
---------

    Los tipos de datos de referencia 
    son aquellos que representan 
    objetos que se almacenan en la 
    memoria y que requieren la 
    asignación de memoria dinámica. 
    Estos tipos de datos se definen 
    mediante clases, interfaces, 
    estructuras y enumeraciones.

* object: representa cualquier tipo de objeto.
* string: representa una cadena de caracteres Unicode.
* class: define una clase, que es una plantilla para crear objetos.
* interface: define una interfaz, que es una colección de métodos y propiedades que una clase puede implementar.
* struct: define una estructura, que es un tipo de valor que contiene un conjunto de campos.
* enum: define una enumeración, que es un tipo de valor que consta de un conjunto de constantes con nombre.

Varibles
-----

    Las variables en C# se pueden declarar sin inicializar.
    No se puede usar una variable sin haberla inicializado

    Además las variables se pueden inicializar en linea

    

###### Sintaxis:
    TipoDeDato nombre;
    int nombre;

    nombre=dato;
--------------

    inicialicación en linea
    int variable1;
    int variable2;
    int variable3;
    int variable4;
    variable1=variable2=variable3=variable4=dato;
---------
    declararación en linea

    int var1,var2,var3,var4;
-----
    Declaración implicita:

    var variable=tipo de dato;

    Variable tiene el tipo de dato que C# detecta durante la compilación, pero debe ser inicializada a la ves que se declara




Operadores Aritméticos
------
| nombre | simbolo | utilidad |
|--------|---------|----------|
| Suma |     + |Concatenar strs, incremento ++|
| Resta |    - |Decremento --|
| Multiplicación | * |        |
| División |      / |         |
| Módulo |        % |         |
|incremento|+=, -=| incrementar y asignar|


Casteo de datos (casting)
---

Sirve para convertir de un tipo de dato a otro 

    double varibale= 9.5;
    int variable2;

    variable2= (int) variable
-------
    Lo que se hace es poner entre parentesis como prefijo el tipo de dato al que se quiere castear

-------

    Se pueden hacer conversiones implicitas entre tipos de datos compatibles como double y float, o un int casteado a double, pero no double a int.

##### Conversiones de Texto a número


Los textos son objetos de tipo string, no son tipos de datos primitivos.

###### Sintaxis:
    
    int variable = int.Parse("num")

Constantes
--
A diferencia de las variables el valor de las constantes no cambiará nunca. esto es útil cuando algún valor es muy usado durante todo el programa.

###### Sintaxis:
    
    const tipo nombre = dato
    
    Siempre se deben inicializar a la vez que se declaran. 

Métodos
--
###### ¿que son?
Los métodos son un grupo de sentencias a las que se dan un nombre indentificativo que realizan una tarea en concreto. 

###### ¿Para que sirven?
Para realizar una tarea en concreto en un momento determinado. Un método no realiza su tarea hasta que no es llamado

###### Sintaxis

    Tipo devuelto nombre (Parámetros){
        cuerpo del método
    }
###### Ejemplo

    int sumaNumeros(int x, int y){
        int resultado = x + y;
        return resultado;
    }

    void sumaNumeros(){
        int num1=7;
        int num2=9;
        int resultado= num1+num2
        console.WriteLine(resultado)

    }
###### Comentarios
    Además se puede agregar un modificador de acceso al inicio del método. 

###### Método main
    public class Program
    {
        public static void Main(string[] args)
        {
            
        }
    };
EL método main es siempre lo primero que el programa ejecuta. Es void porque no regresa ningún valor. Y es static porque no necesita ningún objeto para ejecutarse. 

Funciones Flecha
--

###### sintaxis
    modificador tipo nombre (parametros)=> operación

Alcance de métodos y variables
--

tipos:
* local
* clase

Sobrecarga
--

    Para que exita sobrecarga hay dos o más métodos con diferente números de parámetros o de diferente tipo

Operadores booleanos y condicionales
--
| simbolo | significado| 
|---|---|
|==| igual que |
|!=| diferente que|
|< |menor que |
|<=| menor o igual que |
|>|mayor que|
|&&|and|
|\|\||or|

Condicional If
--
Es una estructura de control de flujo

###### sintaxis

    if (condition)
    {
        bloque de código
    
    }
    else if(conditions)
    {
        Bloque de código
    }
    else
    {
        bloque de código
    }

###### Otra forma es:
    
    if (condition) una sola linea de código;
    else if (condition) una sola linea de código;
    else una sola linea de código;

Switch
--
Switch en C# es una estructura de control que permite evaluar una expresión y ejecutar diferentes bloques de código dependiendo del valor que tenga esa expresión. Es como tener varias opciones de caminos y elegir uno en función del valor que tenga una variable.

###### Sintaxis
    Switch(expresión de control)
    {
        case expresión constante:
            código a realizar
            break;
        case expresión constante:
            código a realizar
            break;
        ...
        default: 
            código a realizar
            break;
    }
###### Obserbaciones
* Cada expresion constante ha de ser única
* Solo se puede usar el switch para evaluar:
    - int
    - char
    - string

Bucles while
-

Bucle indeterminado
###### sintaxis
    while (condition)
    {
        bloque de código
    }

Bucle Do while
-
Sirve para que el bucle indepedientemente de las condiciones se ejecute al menos una vez

###### Sintaxis 

    do{
        bloque de código
    }
    while(conditión);

Excepciones
--

Son errores en tiempo de ejecución del programa que escapan al control del programados.

* Memoria corrutpa
* Desbordamiento de pila
* sectores de discocuro defedtuosos
* Acceso a ficheros inexistentes
* Conexiones a BBDD interrumpidas

#### Bloques try catch

###### Sintaxis
    try
    {
        bloque de código
    }
    catch(Excepción nombre)
    {
        bloque de código
    }
    catch(Excepción nombre)
    {
        bloque de código
    }

Herencia de excepciones
--
    Las excepciones tienen una jerarquia.
    Exception
    System
    FormatException, OverflowException,... etc.

Creación de Clases e instancia de objetos
--

En C# primero se debe crear el objeto y luego se hace la instancia de la clase, su sintxis sería:

###### Sintaxis

    class Nombre() //nombre empieza con mayuscula
    {
        metodoDeAcceso 
    }

Modificadores de accso
--

https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/keywords/access-modifiers

public
private
protected 
internal
protected internal
file

Valor de retorno
--

Este puede ser un tipo de dato o un objeto. 

Constructores
--
Estos tienen la finalidad de dar estado inicial a un objeto

###### Sintaxis:
    class NameClass
    {
        type private property1;
        type private property2;
        type private property3;
        NameClass()
        {
            property1 = value1;
            property2 = value2;
            property3 = value3;
        }
        NameClass(type property1Object, type property2Object, type property3Object)
        {
            property1 = type property1Object;
            property2 = type property2Object;
            property3 = type property3Object;
        }
    }

Tenemos dos constructores, uno que establece propiedades iniciales al objeto, 

Getters & Setters
--

Su función y  sintaxis son claras desde su nombre . 
Aunque se debe mencionar Que el nombre es relevante por convención

##### Sintxis:

    type setName(type parameter1Name type parameter2Name)
    {
        property1 = parameter1Name;
        property2 = parameter2Name;
    }

Además es natural pensar que por casa setter tengamos un getter. 
También es importante que las varibles que hacen referencia a las propiedades del objeto se haga uso de la palabra **.this**.

Programación orientada a objetos
--

para hacer un modelo en .net necesitamos, por convención una carpeta llamda models, esta carpeta tendrá en su interior archivos de clases c# cada una con el nombre se su modelo. 

la sintaxis de una clase sería:

###### Sintaxis:

