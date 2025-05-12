# FLASK

Entorno birtual bat sortu:

```sh
# Crear el entorno virtual (en Python 3)
python -m venv venv

# Activar el entorno (Linux/macOS)
source venv/bin/activate

# Activar el entorno (Windows)
venv\Scripts\activate
```

Flask instalatu

```sh
pip install flask
```

app.py sortu

```python title=""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

Exekutatu:

```sh
python app.py
```

```sh
flask run
```

Gorde requirements:
```sh
pip freeze > requirements.txt
```

.gitignoren sartu
```
git init
# Si no existe el archivo:
touch .gitignore

# Edítalo (con nano, VSCode, etc.) y añade las reglas:
nano .gitignore
```
nanon jarri zein diren gitignorekoak
```nano
# Ignorar el archivo .env
.env

# Ignorar la carpeta venv
venv/
```

git
```nano
git add .
git commit -m "egindako aldaketak"
git push
```

remotoa
```
git remote add origin <github link>
git push --set-upstream origin master #Lehen aldiz
```

FLASK EGITURA
```text
mi_proyecto_flask/
│
├── venv/                    # Entorno virtual (ignorado por Git)
│
├── app/                     # Paquete principal de la aplicación
│   ├── __init__.py          # Inicializa la app y define factory pattern
│   ├── routes.py            # Rutas principales
│   ├── models.py            # Definición de modelos de base de datos
│   ├── templates/           # Plantillas HTML
│   │   ├── base.html        # Plantilla base
│   │   ├── index.html       # Plantilla específica
│   │   └── errors/         # Plantillas de error
│   ├── static/              # Archivos estáticos
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── utils/               # Utilidades adicionales
│       └── helpers.py       # Funciones auxiliares
│
├── migrations/              # Migraciones de BD (si usas Flask-Migrate)
│
├── tests/                   # Tests unitarios
│   ├── __init__.py
│   └── test_routes.py
│
├── config.py                # Configuraciones (dev, prod, testing)
├── .env                     # Variables de entorno (ignorado)
├── .env.example             # Plantilla de variables
├── .gitignore               # Archivos ignorados por Git
├── requirements.txt         # Dependencias
└── run.py                   # Punto de entrada (opcional para desarrollo)
```

DATU BASEA

```sh
pip install flask-sqlalchemy flask-migrate
```

SORTU ETA MIGRATU
```sh
# Inicializa la base de datos (primera vez)
flask db init  # Crea carpeta 'migrations'

# Genera primera migración
flask db migrate -m "Creación tabla User"

# Aplica los cambios
flask db upgrade
```