# Python - Microsoft Learn

### Cursos de Python 🐍

- Ejecutar un fichero:

```
python src/app.py
```

- Comandos Entorno virtual:

```
# Crear un entorno virtual 'env'
python -m venv env

# Ejecutar un entorno virtual (windows)
env\Scripts\activate

# Ejecutar un entorno virtual (Linux)
source env/bin/activate

# Desactivar el entorno virutal
deactivate
```

- Comandos pip:

```
# Instalar una librería (python-dateutil)
pip install python-dateutil

# Ver los paquetes instalados
pip freeze

# Ver la versión de un paquete
pip freeze python-dateutil

# Crear un archivo requirements.txt con todos los paquetes que el programa necesita
pip freeze > requirements.txt

# Restaurar un proyecto. Necesita tener creado el fichero 'requirements.txt'
pip install -r requirements.txt

# Instalar una versión específica de un paquete
pip install python-dateutil===2.8.0

# Actualizar un paquete
pip install python-dateutil --upgrade

# Actualizar los parches (*) de una versión 2.7 instalada
pip install "python-dateutil==2.7.*" --upgrade

# Desinstalar un paquete
pip uninstall python-dateutil
pip freeze > requirements.txt

# Desinstalar todos los paquetes de la lista
pip uninstall -r requirements.txt -y
pip freeze > requirements.txt
```
