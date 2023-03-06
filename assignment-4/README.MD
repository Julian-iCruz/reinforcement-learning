#  **Reinforcement Learning** - *ISIS 4222* - *Monte Carlo*

## 1. INSTALACIÓN PAQUETE DISTRIBUIBLE

En este repositorio encontrará la solución al ***Assignment-4*** correspondiente a ***Monte Carlo*** realizado por el estudiante ***Julian Iguavita***.


Para la ejecución de este programa se ha creado un módulo personalizado el cual se encuentra en la carpeta **ReinforcementLearning** la cual se encuentra en a raíz de este repositorio, para la instalación de este módulo se deben seguir los siguientes pasos:

**1. Creacion de entorno virutal**

Es importante aislar el entorno de ejecución del proyecto, por ende con ayuda de **virutalenv** se logra este propósito.

```bash
pip3 install virtualenv
```

Se crea un entorno virtual, se activa el entorno y se instalan los modulos base con ayuda del archivo **requirements.txt**

```bash
virtualenv env
```

```bash
source ./env/bin/activate
```

```bash
pip install -r requirements.txt
```

Finalmente debemos instalar el modulo creado, para ello seguimos los siguientes pasos estando en la raiz del repositorio.

```bash
cd ReinforcementLearning
```

```bash
python3 setup.py install
```

Con esto ya podremos hacer uso de nuestro módulo **ReinforcementLearning**, si desea ver que contiene internamente el paquete puede dirigirse a cada uno de los **.py** que se encuentran en el path: **ReinforcementLearning/ReinforcementLearning**.

## 2. EJECUCIÓN MONTE CARLO

Para ver en funcionamiento el algorirmo de Monte Carlo debemos ejecutar el archivo ***mcm.py***

```bash
python3 mcm.py
```

La salida de la ejecucion de este archivo tiene, el GridWorld usado, Las politicas para cada casilla dependiente y la cantidad de pasos realizados para llegar a esta politica y finalmente la qtable que muestra V(casilla (x,y)) para cada una de las posibles politicas en la casilla.

### Gridworld

![GridWorld.](/assignment-4/imgs/GridWorld.jpg "GridWorld.")

### Policy

![GridWorld.](/assignment-4/imgs/Policy.jpg "GridWorld.")

### QTable

![GridWorld.](/assignment-4/imgs/qTable.jpg "GridWorld.")

## 3. EJECUCIÓN MONTE CARLO ipynb

De igual manera se puede testear el algoritmo y realizar algunas variaciones desde el archivo ***assigment-4.ipynb*** en este tambien se encuentran las repuestas a las preguntas hehcas en la guia.

