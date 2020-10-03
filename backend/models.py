from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models

class Reservable(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return f'{type(self).__name__} {self.numero}'

    class Meta:
        abstract = True

    def clean(self):
        if type(self).objects.filter(numero=self.numero).exists():
            raise ValidationError(f'Ya existe {type(self).__name__} con este numero')

class Carpa(Reservable):
    pass

class Sombrilla(Reservable):
    pass

class Estacionamiento(Reservable):
    pass

class Reserva(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class ReservaDetalle(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    carpa = models.ForeignKey(Carpa,on_delete=models.CASCADE,null=True,blank=True)
    sombrilla = models.ForeignKey(Sombrilla,on_delete=models.CASCADE,null=True,blank=True)
    estacionamiento = models.ForeignKey(
        Estacionamiento,on_delete=models.CASCADE,null=True,blank=True
    )
    reserva = models.ForeignKey(Reserva, related_name='detalles', on_delete=models.CASCADE)

    def clean(self):
        reservables = [
            self.carpa,
            self.sombrilla,
            self.estacionamiento,
        ]
        if len(list(filter(None, reservables))) != 1:
            raise ValidationError('Solo un reservable por reserva')

        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError('La fecha de inicio no puede ser menor a la fecha final')
