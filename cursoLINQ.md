#CURSO LINQ

Que es LINQ?
--
por las sigral "languaje integrated native query" es una extensión a c# en .net para hacer consultas con el mismo lenguaje que está utilizando y no usar un lenguaje separado como SQL, tiene una sintaxis similar a SQL pero se integra directamente con el lenguaje además permite hacer consulas más complejas como bases de datos, objetos y servicios web 

ejemplo
 var unTomate = form t in ArraydeStrings where t == "Tomate" select t;

 ArraydeStrings.Where(t=>t == "Tomate")

Programación declarativa
--

En LINQ, las consultas se escriben en un estilo declarativo utilizando la sintaxis de consulta integrada en el lenguaje de programación. En lugar de escribir código que especifique cómo se deben realizar las operaciones de filtrado, ordenación ,etc. Los desarrolladores pueden simplemente declarar las operaciones que se deben realizar y LINQ se encarga del resto.

Esto nos permite no tener que escribir paso a paso que pasos se deben realizar para hacer una consulta. 
###### ejemplos:
###### Declarativa 
 const array1=[1,2,3,4];
array1.forEach(element => console.log(element))

###### imperativa:
for (let i=0, i<array1.lenght;i++ )
{
     console.log(element)
}
###### Declarativo
var listOfNumbers = new int[] {1,2,3,4,5};
var item1= listofNumbers.FirstOrDefault(p= p=1);
Console.WriteLine(item1);
###### Imperativo
var listOfNumbers = new int[] {1,2,3,4,5};
for (int i = 0; i < list0fNumbers.Length; i++) 
{
  if(listOfNumbers[i]==1) Cosole.Writeline(listOfNumbers[i])
}
                        Api LINQ
                            |
                            |
        Enumerable -------------------- Querable 


