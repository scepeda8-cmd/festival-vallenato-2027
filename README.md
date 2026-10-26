# Sistema Web de Votaciones

Festival de la Leyenda Vallenata 2027

## Tecnologías utilizadas

- Python
- Django
- MySQL
- HTML
- CSS

## Funcionalidades implementadas

- Registro de usuarios
- Inicio de sesión
- Cierre de sesión
- Administración mediante Django Admin
- Gestión de Ediciones
- Gestión de Categorías
- Gestión de Votaciones
- Gestión de Opciones
- Consulta dinámica de información desde MySQL

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/scepeda8-cmd/festival-vallenato-2027.git
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar migraciones:

```bash
python manage.py migrate
```

Ejecutar servidor:

```bash
python manage.py runserver
```