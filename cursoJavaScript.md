# Indice:
 - Caracteristicas de JS
 - Tipos de datos
 - FUNCIONES BÁSICAS
 - ARRAYS
 - BUCLES
 - FUNCIONES
 - POO
 - HERENCIA
 - NETODOS ESTÁTICOS
 - GETTERS & SETERS 
 - MÉTODOS DE CADENA 
 - TRANSFORMERS ARRAYS METHODS
 - ACCESORS ARRAYS METHODS
 - REPETITION ARRAYS METHODS 
 - MATH
 - MATH.PROPERTIES
 - CONSOLA
 - DOM
 - SELECTION ELEMENT METHOD  
 - SELECTION QUERRY METHOD 
 - MODIFY ELEMENTS
 - GLOBAL ELEMENT ATRIBUTES  #
 - INPUT METHOD  
 - LIST
 - Obtencion #modificaciòn de elementos 

# Caracteristicas de JS

    1.- orientsdo a objetos:
    2.- imperativo: Es este tipo de lenguajes, las instrucciones se ejecutan unas tras otras, 
    3.- Case Sensitive: diferencia entre mayusculas y minuculas
    4.- Basado en prototipos: los objetos son creados nativamente por el lenguaje
    5.-Tipado Debil: puede cambiar el tipo de dato de una variable en cualquier momento 
    6.- Lenguaje dinámico: donde el intérprete asigna a las variables un tipo durante el tiempo de ejecución 
            basado en su valor en ese momento.
    7.- Es posible usr código html en variables de java script
            let variable =`<p style="color: black"> algún texto </p>`
Ecmascript: se encarga de estandarizar java script
# Tipos de datos

    1.-string= 'cadena',"cadena",
    2.-Number= 19
    3.-Bool=true, false, 0 , 1  
    4.-Symbol = son datos únicos. se usan para crear propiedades privadas 
    5.-Undefined, null, Nan
        var num; -> Undefined
        let num= null;
        
variables:
    var: local 
    let: global 
    const: constante
    *podemos declarar variables e inicializarla depués
# FUNCIONES BÁSICAS

    alert() crea una alerta en pantalla imprimiendo lo que se pasa por parámetro
    prompt("algún texto");   es un input,imprime lo que se pase por parámetro ,guarda en una variable lo que recibe.
    document.write(frase);
    variable1.concat(variable2);
operadores:
    Aritméticos:+  suma 
                ++ incremento
                -  resta
                -- decremento
                *  multiplicación
                /  división
                %  resto 
                ** elevación
    Asignación:+=,-=,*=,/=,%=,**=
Concatenación:
    significa unir strings.
    dadas dos variables de tipo string basta con usar el operador +
    ejemplo:
            saludo: "hola, alex"
            pregunta: ¿como estás?
            frase =saludo +pregunta
    otra forma es con números. dados dos números debemos castear los datos. una forma es 
        var numero1= 1;
        var numero2= 2;
        frase =""+ numero1 + numero2
    otra forma que es útil cuando se tiene un string es usando la función concat()
        var frase1= frase1
        var frase2= frase2
        data= frase1.concat(frase2)
    y por último tenemos ${}: con backticks 
        frase =´bienvenido ${variable}`
        Esto es útil para escribir html:
            `<h1></h1>
            <div></div>`
operadores de comparación:
    equal a==b;
    enequal a!=b;
    identitya===b;
    non-identity a!==b;
    greate than a>b;
    greate than or equal a>=b;
    less than a<b;
    less than or equal a<=b;
operadores logicos:
    and &&;
    or ||
    not !
Camel Case:
    listooooYaMeLoSé;
Condicionales:
    if
    else if
    else
        #### sintaxis:
                if (condition){
                    block content
                }
Ejercicio 1:
    tres chicos de 23 años conpran helado, cada uno tiene distintas cantidades de dinero, ellos quieren el helado más caro posible.
    si hay dos con el mismo precio mostrar lo mismo. 
    indicar el cambio. 
# ARRAYS
#### Sintaxis: 
    let info=["Alex", 24, "Ciudad universitaria"];
    let array=[]; //si se desea hace run array vacio
acceder a sus elementos: 
    info[i]

ARRAYS ASOCIATIVOS (diccionarios en python)

#### Sintaxis:
    let info={key1:"value1",
        key2:"value2",
        key3:"value3",
    }
Acceder a sus elementos:
    info["key1"]
# BUCLES
Partes de un bucle:
    + declaración
    + aumento ó decremento
    + condición
#### Sintaxis:
    while (condition){
        block content
    }
    -------------------------
    do{
        block content
    }
    while(condition)

    break;
    -------------------------
    let i=0;
    for (let i =0; stop condidion; increment or decrement) {
        block content
    }
    continue;

    array=[value1,value2,value3,valuen]
    for (value in array){
        block content
        //esto recorre el arrayy guarda el indice de cada elemento en la variable value
    }
    for (value of array){
        block content
        // esto recore el array y guarda el valor de cada elemento en la variable vlaue 
    }
Sentencia label:
    forName:
    for (let i =0; stop condidion; increment or decrement) {
        block content
        break forName;
    }
# FUNCIONES

#### Sintaxis:
    function name(parameters){
        block content
        return valueToReturn
    }
Funciones flecha:
    const name = parameter => line content
    
    Si se usan más parámetros, van entre parentesis, incluso si no usa ninguno.

# POO
### Pilares:
    Abstracción
    Modularidad
    Polimorfismo 
    Encapsulamiento
#### Sintaxis:
    class name {
        contructor (parameter1, parameter2){
            this.property1=parameter1;
            this.property2=parameter2;
        }
        metod(){
            block content
        }
    }
    const= new name("parameter1","parameter2");
    name.metod()

# HERENCIA
#### Sintaxis:
    class name {
        contructor (parameter1, parameter2){
            this.property1=parameter1;
            this.property2=parameter2;
        }
        metod(){
            block content
        }
    }

    class Name2 extends Name 1{
        constructor(parameter1, parameter2, anotherParameter){
            super(parameter1, parameter2);
            this.anotherParameter
        }
        anotherMetod(){
            block content
        }
    }
    const= new name1("parameter1","parameter2");
    name1.metod()
    const= new name2("parameter1","parameter2");
    name2.anotherMetod()
#  NETODOS ESTÁTICOS
### Uso:
    Sirve para ejecutar métodos sin instanciar una clase
#### Sintaxis: 
    class Name2 extends Name 1{
        constructor(parameter1, parameter2, anotherParameter){
            super(parameter1, parameter2);
            this.anotherParameter
        }
        static anotherMetod(){
            block content
        }
    }
    name2.anotherMetod()
#  GETTERS & SETERS 
#### Sintaxis:
    class Name2 extends Name 1{
        constructor(parameter1, parameter2, anotherParameter){
            super(parameter1, parameter2);
            this.anotherParameter
        }
        set setMetod(newParameter){
            this.parameter3=newParameter
        }
        get getMethod(){
            return property
        }
    }
    name2.setMetod(something )


# MÉTODOS DE CADENA 
let cadena="Esto es una cadena de prueba"
let resultado;
document.write(resultado)
Funciones relacionadas:
    cadena1.concat(cadena2);         //concatena dos cadenas 
    cadena1.startWith(cadena2);      //verifica su una cadena empieza con otra que se para por parámetro
    cadena1.endsWith(cadena2);       //verifica si una cadena termina con otra
    cadena1.include(cadena2);        //verifica si una cadena está contenida en otra
    cadena1.indexOf(cadena2);        //regresa el indice donde se encuentra la primera letra de una cadena solo 
                                        si se encuentra en la primera cadena 
    cadena1.lastIndexOf(cadena2);    //regresa el indice donde se encuentra la última letra de una cadena solo 
                                        si se encuentra en la primera cadena
    cadena1.padStart(n,caracter);    //rellena la cadena al comienzo con la cantidad total n con los caracteres en 
                                        caracter
    cadena1.padEnd(n,caracter);      //rellena la cadena al final con la cantidad total n con los caracteres en 
                                        caracter
    cadena1.repeat(n);               //repite la cadena tantas veces como n indica 
    cadena1.split("caracter");        //divide una cadena según el caracter pasado por parámetro y regresa un array.
    cadena1.substring(i,j);           //crea un nuevo string, i representa la posición de inicio y j la posisción 
                                        final
    cadena1.toLowerCase();            //convierte las mayusculas a minisculas
    cadena1.toUpperCase();            //convierte las mayusculas a mayussculas
    cadena1.toString();               //Castea a string
    cadena1.lenght;                   //devuelve la longitud de la cadena
    cadena1.trim();                   //remueve los espacios de una cadena
    cadena1.trimEnd();                //remueve los espacios al final de una cadena
    cadena1.trimStart();              //remueve los espacios al inicio de una cadena
# TRANSFORMERS ARRAYS METHODS
### ### Definition:
    This methods transform the original array. dont create a new object
array=["element1","element2","element3"]
Funciones Relacionadas
    array.pop();                     //elimina el último elemento de un array devuelve el valor eliminado
    array.shift();                   //elimina el primer elemento de un array devuelve el valor eliminado
    array.push();                    //agrega un elemento al final de un array devuelve la cantidad de elementos 
                                        que tiene el array permite agregar más de uno
    array.reverse();                 //invierte el orden del array
    array.unshitf(array);            //agrega varios elementos al inicio del array
    array.sort();                    //ordena de menor a mayor 
    array.splice(i,n,array);         //Elimina o remplaza n elementos desde la posición i y remplaza dichos 
                                        elementos con los pasados adminte indices negativos.
# ACCESORS ARRAYS METHODS
### Definition:
    This methods transform the original array. dont create a new object
    array=["element1","element2","element3"]
    Funciones Relacionadas
    array.join(string);             //Crea un string a partir de los elementos del array separado por el string 
                                        pasado 
    array.slice(i,j);               //devuelve un array formado por los elementos que van desde la posición i 
                                        hasta j
    array.includes(element);        // devuelve el índice donde se encuentra el elemento pasado por parámetro
    array.lastIndexOf("string");    //devuelve el último elemento igual al string pasado por parámetro
# REPETITION ARRAYS METHODS 
let numeros =[]
Funciones relacionadas:
    array.filter(arrayElement=>{line content});
                                    //regresa un array.
    array.forEach(arrayElement=>{line content});
    }
# MATH

Es parte de una clse. Sus métodos son:

Métodos Relacionados:
    let int= Math.sqrt(num);
    let int= Math.max(array);
    let int= Math.min(array);
    let int= Math.random();         //devuelve un número entre 0 y 1
    let int= Math.round(num);       //devuelve el entero más cercano 
    let int= Math.floor(num);
    let int= Math.fround(float);    //devuelve el número de precisión simple más cercano 
    let int= Math.trunc(float);     //elimina los decimales

# MATH.PROPERTIES

Marh.PI;
Math.SQRT2;
Math.SQRT_2;
Math.LN10;
Math.LN2;
Math.LOG10E;
Math.LOG2E;

# CONSOLA



# DOM

### Definition:
    DOM: Document Object Model 
            es un documento que nos permite representar todos los elementos de un archivo html, 
    Nodo: son las etiquetas individuales html
        Tipos:
            Document: el nodo document es el nodo raíz , a partir del cual derivan el resto de nodos.
            Element: nodos definidos por etiquetas html.
            Text: es el texto dentro de un element.
            Atribute: los atributos de las etiquetas html, en javascript no los tomaremos como nodos, si no como 
                    información asociada al nodo de tipo element
            Comentarios y otros: comentarios y otros elementos como declaración doctype en la cabecera entre otros

# SELECTION ELEMENT METHOD  

#### Sintaxis:
    document.getElementById("element")          //selecciona un elemento por id
    document.getElementByTagName("element")     

# SELECTION QUERRY METHOD 

#### Sintaxis:
    document.querrySelector(".class")
    document.querrySelector(" #id ")        

    // regresan un node list

#     MODIFY ELEMENTS

    const variable=document.querySelector(".class");
#### Sintaxis:
    variable.setAttribute("Atribute","newAtribute")
    variable.getAttribute("Atribute","newAtribute")
    variable.removeAttribute("Atribute","newAtribute")

#  GLOBAL ELEMENT ATRIBUTES  #

Estos métodos son aplicables a cualquier elemento html
    
    const variable=document.querySelector(".class");
### Métodos Relacionados:
    variable.setAttribute("contentEditable","true")
    variable.setAttribute("set","rtl") 
    variable.setAttribute("hidden","true")
    variable.setAttribute("tabindex","0")    //sirve para establecer un orden en que se puede seleccionar con tab
    variable.setAttribute("title","text")    //cambiar el título de un elemento

    Existen más atributos globales. 
########################################      estudiarlos      #########################################

#  INPUT METHOD  

const input=document.querySelector(".input");

Métodos Relacionados:
    input.className         //Regresa el nombre de la clase del input
    input.value             //REgresa el valor ingresado en el input
    input.type
    input.accept            //tipo de archivo que acepta el input. por ejemplo xml o png etc.
# LIST
const elemento=document.querrtSelector()

Metodos relacionados:
elemento.classList.add(".class"); //añade una clase a un elemetno
elemento.classList.remove(".class");//quita una clase a unn elemento
elemento.classList.item(i);//devuelvela clase del elemento en el indice i
elemento.classList.contains(".class"); //devuelve tru o false si el elemento contiene la clase seleccionada
elemento.classList.toggle("class","true") en caso de tener la clase, la quita y viceversa. mientras que si el segundo parametro es true la deja si la tiene y la pone si no la tiene y viceversa
elemento.classList.replace("class1", "class")//ramplaza la clase 1 por la clase 2, en caso de no contener la clase 1 devuelve false

# Obtencion modificaciòn de elementos 
textContent //muestra todo el texto visible
innerHTML //muestra todo el contenido HTML
outherHTML //mestra todo el contenido tanto de texto como html

# 



        