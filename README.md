# Balneario

Balneario es una app web para administrar reservas en un balneario.

## Requisitos

- Python 3.8.x
- Node.js 12.18.x

## Instalación

Use ```pipenv``` para instalar las dependencias necesarias para el backend.

```
pip install pipenv
pipenv install --dev
```

Use ```npm``` para instalar las dependencias necesarias para el frontend.

```
cd frontend/angularapp
npm i
```

Ejecutar las migraciones desde la raiz del proyecto.

```
pipenv run migrate
```

## Uso
1. Iniciar el frontend ejecutando ```npm start``` desde la carpeta frontend/angularapp.
2. Desde la raiz del proyecto ejecutar ```pipenv run runserver```.
3. Acceder desde http://localhost:4200/.
