Para el correcto funcionamiento del programa, las primeras acciones que realize fueron:

    .Crear la carpeta contenedora Proyecto

    .Realizar un pip install django dentro del shell del Proyecto para poder utilizar el framework

    .Una vez instalado django ,tuve que hacer un django-admin startproyect, para darle inicio al proyecto.

    .Ahora procedi a realizar un python manage.py startapp, para comenzar con la app.

    .Hay que agregar la app en el setting.py en donde estan las INSTALLED_APPS, yo agregue 'Proyect.apps.ProyectConfig' al final de las apps

    .Este proyecto fue realizado con la version 4.1.2 de django.

Estos son los pasos que realize para darle inicio a mi proyecto, luego de esto me dedique a relizar el modelo, views, urls y templates.

    .En primer lugar comenze creando el modelo, el cual se crea en el file models.py. Los modelos son quienes contienen los campos y comportamientos esenciales de los datos que está almacenando. Generalmente, cada modelo se asigna a una sola tabla de base de datos. En mi caso utilize un solo modelo llamado Empleado, con los atributos de name, last_name y area que son atributos de tipo ChardField, utilize un e-mail el cual es un EmailField, un date como fecha que es un DateField y finalmente un avatar que es una ImageField.

    .Una vez creado el modelo, hay que hacer un python manage.py makemigrations que se encarga de crear nuevas migraciones en función de los cambios que haya realizado en sus modelos, inmediatamente realizada la makemigrations hay que utilizar el comando python manage.py migrate que es el encargado de aplicar las migraciones.

A partir de este punto ya el proyecto esta listo para comenzar a trabajar con las views, templates y url.

    .