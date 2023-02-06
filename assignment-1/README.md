# 0. Índice

El ejercicio esta compuesto por 3 archivos

* main.ipynb
* main.py
* requirements.txt

# 1. requirements.txt

Tiene los módulos que son necesarios para ejecutar un notebook en local con ayuda del kernel de Jupyter. En caso de tener instalado el entorno de **Anaconda** no es necesario instalar los módulos de requirements.txt.

Se recomienda tener un entorno virtual creado donde se instalen los módulos a usar. Para ello:

1. Se crea el entorno virtual donde ***<virtual_env_name>*** se remplaza por el nombre que se le desee poner al mismo.

```bash
virtualenv <vitual_env_name>
```

2. Se activa el entorno virutal para este caso en ***linux*** (revisar como activar entorno virtual en Windows).

```bash
source ./<vitual_env_name>/bin/activate
```

3. Se descargan los modulos del requirements.txt

```bash
pip install -r requirements.txt
```

Una vez realizado esto ya se tiene el entorno virtual listo para la ejecución de notebooks de manera local.

# 2. main.ipynb

Contiene el código realizado de bandido de greedy, en él se puede ir mirando en los comentarios la lógica que se diseñó dependiente del enunciado de la tarea.

Si ya se tiene instalado el entorno virtual con los módulos necesarios en local o se tiene un entorno de Anaconda, se pueden ejecutar la celda donde se crea la clase ***Bandit*** y la celda donde se crea un bandido y se ejecuta con la función **run()**.

```python
bandit_greedy = Bandit()
bandit_greedy.run()
```

De esta manera obtiene una lista con las recompensas para cada iteración.

# 3. main.py

Adicionalmente se crea un ejecutable el puede ser ejecutando por consola dando a la salida la lista de las recompensas para cada iteración.

```bash
python3 main.py
```