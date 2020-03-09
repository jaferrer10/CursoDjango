from django.db import models

# Create your models here.
class Project(models.Model):
     title = models.CharField(max_length=200, verbose_name='Título')
     description = models.TextField(verbose_name='Descripción')
     image = models.ImageField(verbose_name='Imágen', upload_to="projects")
     link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
     created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
     updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

     # traduce al español la seccion proyectos del panel
     # nombre del campo por el cual va a ordenar y el signo menos al inicio significa orden descendente
     class Meta: 
          verbose_name = "proyecto"
          verbose_name_plural = "proyectos"
          ordering = ["-created"]   


     # muestra el nombre del proyecto en la grilla de proyectos
     def __str__(self):
          return self.title   