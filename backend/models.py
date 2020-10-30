from datetime import date
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

class Item(models.Model):
    RESERVABLES = (
        ('carpa', 'Carpa'),
        ('sombrilla', 'Sombrilla'),
        ('estacionamiento', 'Estacionamiento'),
    )

    numero = models.IntegerField()
    habilitado = models.BooleanField(default=True)
    tipo = models.CharField(max_length=20, choices=RESERVABLES)

    def __str__(self):
        return f'{self.get_tipo_display()} {self.numero}'

    def clean(self):
        if type(self).objects.filter(numero=self.numero, tipo=self.tipo):
            raise ValidationError(f'Ya existe {self.tipo} con este numero')

class Precio(models.Model):
    item = models.CharField(max_length=20, choices=Item.RESERVABLES, unique=True)
    valor = models.FloatField()

    def __str__(self):
        return f'{self.get_item_display()} ${self.valor}'

class Reserva(models.Model):
    ESTADOS = (
        ('impago', 'Impago'),
        ('señado', 'Señado'),
        ('pagado', 'Pagado'),
        ('procesando', 'Procesando')
    )

    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='impago')

class ReservaDetalle(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    item = models.ForeignKey(Item, models.CASCADE, related_name='detalles')
    precio_unitario = models.FloatField(default=0)
    reserva = models.ForeignKey(Reserva, models.CASCADE, related_name='detalles')

    def clean(self):
        if self.fecha_inicio < date.today():
            raise ValidationError('Fecha inicial menor al dia de hoy')
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError('Fecha final menor a inicial')

class MedioPago(models.Model):
    reserva = models.OneToOneField(Reserva, models.CASCADE)

    class Meta:
        abstract = True

class Transferencia(MedioPago):
    comprobante = models.FileField(upload_to='transferencias/')
