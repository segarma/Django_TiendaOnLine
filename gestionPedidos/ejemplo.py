from django.db import models

class MiModelo(models.Model):
    ''' Esta sería una clase típica definiendo un modelo
    derivada desde la clase Model '''

    # Definición de campo
    mi_campo_nombre = models.CharField(max_length=20, help_text='Introduzca documentación')

    # Definición de métodos
    def get_absolute_url(self):
        '''Devuelve la url para acceder a una instancia particular de MiModelo'''
        return reversed('vista_detalle_modelo', args = [str(self.id)])
    # Definición de metadato
    class Meta:
        ordering = ['-mi_campo_nombre']


