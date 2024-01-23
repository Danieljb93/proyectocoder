# proyectocoder

proyecto en django

# para acceder a las urls:

-   ingresar a la url: http://localhost:8000/coder-app/
-   usuario: admin
-   contraseña: admin54321

# Sistema de Gestión de Ventas

Este es un proyecto de una aplicación de gestión de ventas desarrollada con Python y Django. La aplicación permite a los usuarios manejar información sobre vendedores, clientes, productos y registros de ventas, facilitando la gestión de datos en un entorno de ventas.

    * Vendedores: Registro y gestión de información sobre los vendedores asociados a la empresa.
    * Clientes: Mantenimiento de datos de los clientes, incluyendo información relevante para la gestión de ventas.
    * Productos: Registro y control de inventario de productos disponibles para la venta.
    * Ventas y Fechas: Registro de transacciones de ventas con fechas asociadas para un seguimiento detallado.

Instalación

    Clona el repositorio a tu máquina local utilizando el siguiente comando:

    bash

git clone https://github.com/tu_usuario/sistema-gestion-ventas.git

Accede al directorio del proyecto:

bash

cd sistema-gestion-ventas

Instala las dependencias necesarias:

bash

pip install -r requirements.txt

Realiza las migraciones de la base de datos:

bash

python manage.py makemigrations
python manage.py migrate

Inicia el servidor:

bash

python manage.py runserver

Accede a la aplicación en tu navegador web mediante la dirección http://localhost:8000.
