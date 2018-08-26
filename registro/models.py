from django.db import models
from django.utils import timezone

class Animal(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20)
	edad = models.IntegerField()
	fecha_registro = models.DateTimeField(default=timezone.now)
	fecha_adopcion = models.DateTimeField(null=True, blank=True)
	en_adopcion = models.BooleanField(default=True)

	def adoptar(self):
		self.fecha_adopcion = timezone.now()
		self.en_adopcion = False
		self.save()

	def __str__(self):
		return self.nombre
	