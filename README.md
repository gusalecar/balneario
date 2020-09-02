# Balneario

Balneario es una app web para administrar reservas en un balneario.

## Requisitos

- Python 3.8.x
- Node.js 12.18.x

## Instalación

Use ```pip``` para instalar las dependencias necesarias para el backend.

```
pip install -r requirements.txt
```

Use ```npm``` para instalar las dependencias necesarias para el frontend.

```
cd frontend/angularapp
npm i
```

Ejecutar las migraciones desde la raiz del proyecto.

```
python manage.py makemigrations
python manage.py migrate
```

Debe ejecutarse cada vez que algun modelo es cambiado.

## Uso
1. Compilar el frontend ejecutando ```ng build``` desde la carpeta frontend/angularapp.
2. Desde la raiz del proyecto ejecutar ```python manage.py runserver```.
3. Acceder desde http://localhost:8000/acceso.
