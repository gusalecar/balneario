from django.db import models

class Carpa(models.Model):
    id = models.AutoField(primary_key = True)
    ocupado = models.CharField(max_length=10)

    def __str__(self):
        return '{0}.{1}'.format(self.id,self.ocupado)
