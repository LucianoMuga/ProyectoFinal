from django.db import models

from django.db import models

class Empleado(models.Model):
    
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    area = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 200)
    date = models.DateField()
    avatar = models.ImageField(upload_to = "post", null = True , blank = True)
    
    def __str__(self):
        return f"name:{self.name}, id:{self.id}"

