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

Contiene el código realizado de Gridworld, en él se puede ir mirando en los comentarios la lógica que se diseñó dependiente del enunciado de la tarea.

