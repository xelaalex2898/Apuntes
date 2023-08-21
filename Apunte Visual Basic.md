# Visual Basic

    Visual Basic es un lenguaje de programación de alto nivel desarrollado por Microsoft. A continuación, se presentan algunos conceptos básicos del lenguaje:

## Declaración de variables

    En Visual Basic, se utiliza la palabra clave `Dim` para declarar variables. Por ejemplo:


    Dim nombre As String
    Dim edad As Integer
    Declaración de funciones o métodos
    Las funciones y métodos se definen utilizando las palabras clave Function y Sub. Por ejemplo:



    Function CalcularSuma(a As Integer, b As Integer) As Integer
        Dim suma As Integer
        suma = a + b
        Return suma
    End Function

    Sub Saludar(nombre As String)
        Console.WriteLine("¡Hola, " & nombre & "!")  
    End Sub
## Operadores
    Aritméticos: +, -, *, /, % (módulo)
    Relacionales: =, <>, >, <, >=, <=
    Lógicos: And, Or, Not
## Estructura if-elseif-else


    If condicion1 Then
        ' Código si la condición 1 es verdadera
    ElseIf condicion2 Then
        ' Código si la condición 2 es verdadera
    Else
        ' Código si ninguna de las condiciones anteriores es verdadera
    End If
## Estructura for


    For i = 1 To 10 Step 1
        ' Código a ejecutar en cada iteración
    Next
## Estructura while


    While condicion
        ' Código a ejecutar mientras la condición sea verdadera
    End While
## Estructura case


    Select Case variable
        Case valor1
            ' Código si la variable es igual a valor1
        Case valor2
            ' Código si la variable es igual a valor2
        Case Else
            ' Código si la variable no coincide con ninguno de los casos anteriores
    End Select

## Bucles Do Loop

### Do Loop While

    Do
        ' Código a ejecutar al menos una vez
        ' ...
    Loop While condicion
### Do Loop Until
    Do
        ' Código a ejecutar al menos una vez
        ' ...
    Loop Until condicion
## Arrays y Vectores
### Declaración de Arrays
    Dim nombres() As String               ' Array vacío
    Dim numeros(4) As Integer             ' Array con tamaño fijo
    Dim colores() As String = {"Rojo", "Verde", "Azul"}    ' Array inicializado
#### Métodos y Propiedades de Arrays
    Length: Propiedad que devuelve la longitud (cantidad de elementos) del array.
    GetValue(index): Método que devuelve el valor en el índice especificado.
    SetValue(value, index): Método que asigna un valor en el índice especificado.
    Ejemplo:

    Dim numeros() As Integer = {1, 2, 3, 4, 5}
    Dim longitud As Integer = numeros.Length   ' Devuelve 5
    Dim valor As Integer = numeros.GetValue(2) ' Devuelve 3
    numeros.SetValue(10, 0)                    ' Asigna 10 al primer elemento
## Matrices
### Declaración de Matrices
    Dim matriz(,) As Integer                 ' Matriz vacía
    Dim matriz(2, 2) As Integer              ' Matriz con tamaño fijo
    Dim matriz = {{1, 2}, {3, 4}}            ' Matriz inicializada
#### Métodos y Propiedades de Matrices
    GetLength(dim): Método que devuelve la longitud en una dimensión específica.
    GetUpperBound(dim): Método que devuelve el índice máximo en una dimensión específica.
    Acceso a elementos: Se utiliza la sintaxis matriz(fila, columna) para acceder a un elemento específico.
    Ejemplo:

    Dim matriz = {{1, 2}, {3, 4}}
    Dim longitudFila As Integer = matriz.GetLength(0)          ' Devuelve 2
    Dim longitudColumna As Integer = matriz.GetLength(1)       ' Devuelve 2
    Dim valor As Integer = matriz(1, 0)    



