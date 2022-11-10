Pre-requisitos que hay que  tener instalado:

    .Python 3.10.6

    .Gestor de instalacion de paquetes PIP

    .Creador de entornos virtuales para Python

Para el correcto funcionamiento de la app las primeras acciones a realizar son:

    .Crear la carpeta contenedora Proyecto

    .Realizar un:

        . pip install django (dentro del shell del Proyecto para poder utilizar el framework)

    .Una vez instalado django ,tuve que hacer un: 

        .django-admin startproyect (para darle inicio al proyecto)

    .Realizar un: 

        .python manage.py startapp (para comenzar con la app)

    .Hay que agregar la app en el setting.py en donde estan las INSTALLED_APPS, yo agregue 'Proyect.apps.ProyectConfig' al final de las apps

    .Este proyecto fue realizado con la version 4.1.2 de django.

    .Crear superuser:

        .python manage.py createsuperuser
    
    .Iniciar el servidor.

        .python3 manage.py runserver


Funcionalidad del sitio web:
    
    .Es un registro de empleados con sus respectivos datos ,el cual nos permite ver imediatamente nombre, apellido , datos de contacto como celuar ,e-mail ,foto de dicho empleado, legajo, fecha de ingreso, etc.

    .El sitio web cuenta con el login y un register, con el fin de que los empleados o dueños que sean los encargados de contratar o despedir a la gente puedan tener acceso a dicho registros y no cualquier persona.

    .Con respecto al login, para la prubea pueden utilizar:
        .username: Luciano
        .password: 1234
    
    .Luego del register accedes al template principal que es donde se veran detallados algunos datos de los empleados para tenerlos presentes.

    .Si se quiere saber datos mas concretos de las personas en la seccion Detail ,esta absolutamente todo los datos sobre cada uno de los empleados.

    .En caso de modificaciones cuenta con una seccion actualizar, para modificar cualquier tipo de dato sobre cualquier empleado.

    .Cuando esa persona ya no trabaje mas para la empresa tambien cuenta con una seccion la cual lo elimina autamaticamente de la base de datos.

    .Esta web cuenta con un Profile update, el cual sirve para modificar datos sobre el usuario que esta iniciado sesion y utilizando la pagina web.



