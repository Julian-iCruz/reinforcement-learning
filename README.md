#  **Reinforcement Learning** - *ISIS 4222*

En este repositorio encontrará la solución a todos los ***Assignments*** propuestos a lo largo del curso realizado por el estudiante ***Julian Iguavita***.

Cada uno estará desarrollado en cada una de las carpetas que llevan como nombre el número se Assignment correspondiente.

#  Assignment 1 - Bandido Greedy

La definición de los bandidos consiste en crear un agente, como una clase de Python, ***Bandit***. Inicialmente crearemos un bandido con una cantidad de brazos dado por parámetro (por defecto utilizaremos 10 brazos). Cada uno de los brazos del bandido (definidos en una lista ***arms*** como un atributo de la clase) tiene su propia recompensa, la cual asignaremos como un número flotante aleatorio en el rango [-3, 3] (utilizando la función random. uniform (-3,3) de la librería random). Adicionalmente, definimos un atributo de la clase (***reward***) para mantener la recompensa cumulativa del bandido. Inicialmente nuestro bandido tiene dos funciones choose_arm y run.

* ***choose_arm*** no tienen parámetros. Esta función se encarga de seleccionar un brazo a ejecutar, de forma aleatoria, y retorna la recompensa recibida de acuerdo a la fórmula:
 
Retornando la recompensa promedio obtenida por el agente al escoger el brazo dado.

Para poder realizar este cálculo, debemos llevar la cuenta de la cantidad de veces que ha sido escogido cada brazo y la recompensa acumulada de cada brazo. Esta información la definimos como atributos de la clase, en las variables ***occurrences*** y ***cumulative_rewards***, respectivamente. Ambos atributos se definen como una lista de tamaño número de brazos del bandido.

El cálculo de la recompensa primero actualiza las ocurrencias de escoger el brazo seleccionado aleatoriamente, ***arm***. Además, debemos actualizar la recompensa cumulativa (***cumulative_rewards***) de ***arm***, sumando la recompensa correspondiente al brazo (obtenida de la lista de brazos). Finalmente, calculamos ***Qt(a)*** como la recompensa cumulativa sobre las ocurrencias para el brazo dado y retornamos dicho valor. La recompensa global del agente se actualiza con el valor calculado.

* ***run*** no recibe ningún parámetro. Esta función define la cantidad de episodios para los cuales vamos a calcular la recompensa del agente (1000 en nuestro caso) Luego creamos un bandido (***bandit***) y una variable para almacenar la recompensa obtenida en cada iteración (***expected_reward***). Para cada uno de los episodios, ejecutamos el bandido llamando la función choose_arm y guardamos el resultado en la lista de recompensas esperadas. Finalmente retornamos la lista de recompensas para cada iteración (***expected_reward***).
