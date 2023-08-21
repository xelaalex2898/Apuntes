#explicación del problema:
El problema al que nos enfrentamos es un problema de clasificación de imagenes, buscamos entrenar una red neuronal convolucional, para ello elegimos usar una base de datos bien conocida llamada "cifar 100". Es un dataset con 100 clases distintas incluyendo personas. 

#Resultados 
#Modelo 1 
Este modelo lo obtuvimos de la página web Kaggle, fué nuestro primer modelo, es un modelo CNN secuencial. 
Tiene una capa de entrada, solamente 3 capas ocultas y solamente una capa de salida, el optimizador es adam, la funcion de perdida fue categorical cross entropy porque el problema es multiclase y la métrica es accuracy.

cabe mencionar que fue entrenado unicamente con 20 epocas. 
#Objetivos iniciales: 
Nospropusimos como primer objetivo tangible mejorar el accurracy de este modelo. 

#modelo 2 

Este es el mismo modelo que el primero, con una arquitectura parecida, con una capa de entrada, se agregó una capa oculta más y una capa densa, con los mismos hiperparámetros, mismo optimizador, misma funcion de perdida y misma métrica, con la diferencia de que se usaron 100 epocas para su entrenamiento. 


#modelo 3 
###Arquitectura 
La arquitectura del modelo comienza con una capa de entrada que coincide con la forma de los datos de entrenamiento.

Luego, se aplican dos capas de convolución con 64 filtros, seguidas de capas de normalización y activación ReLU para extraer características de las imágenes.

Después de cada capa de convolución, se aplica una capa de agrupación máxima (MaxPooling) para reducir el tamaño de las características.

Se agrega una capa de dropout después de la capa de agrupación máxima para regularizar el modelo y evitar el sobreajuste.

Se repite el patrón de capas de convolución, normalización, agrupación máxima y dropout dos veces más, pero ahora con 128 filtros en cada capa de convolución.

Luego, se agrega otra capa de convolución con 256 filtros seguida de normalización y dropout.


Finalmente, se aplana la salida y se conecta a una capa totalmente conectada con 512 neuronas y activación ReLU.

Se agrega una capa de dropout y, finalmente, una capa de salida con 100 neuronas y activación softmax, que representa las clases de salida para la clasificación de 100 categorías diferentes en CIFAR-100.


#Justificación

Primero probamos en crear más capas para hacer una red más profunda
empezamos con La inclusión de capas densas consecutivas con funciones de activación ReLU, normalización por lotes (BatchNormalization) y dropout como parte de una estrategia de regularización. La regularización ayuda a reducir el sobreajuste y mejorar la generalización del modelo. 
Las capas de dropout permiten "desactivar" aleatoriamente conexiones entre neuronas, evitando la dependencia excesiva entre ellas. 
La normalización por lotes también puede ayudar a estabilizar y regularizar el modelo.

Con este cambio nos dimos cuenta que a una cantidad baja de epocas, en especifico una cantidad de 10 epocas el modelo tenía el mismo rendimiento que sus antecesores, especificamente del 49% de accuracy, por lo que supimos que ibamos por buen camino.
las gráficas nos mostraron que teníamos sobreajuste desde las epocas más tempranas, por lo tanto concluimos que podríamos aumentar el parametro de dropout, lo que significa que el modelo apagará el 45% de las neuronas en cada iteración con la finalidad de evitar el ovearfitting.

una vez llegados al limite nos propusimos aumentar la cantidad de epocas notamos que con 30 epocas teníamos un accuracy del 60%, lo cual ya representa un avance significativo comparado con el primer modelo, sin que este modelo sea conclusivo para nuestras espectaivas de obtener un mejor modelo. 

#Que podemos mejorar?

Buscar hiperparametros óptimos en el modelo actual ya que aún tenemos algo de sobreajuste. 

Tratar las técnicas Model Saving y Checkpointing para guardar las epocas en las que tuvo un mejor desempeño nuestro modelo y descartando las epocas donde el desempeño fué bajo

Si esto no es suficiente trataremos la técnica de Tranfer learning luego de encontrar un modelo preentrenado. 





