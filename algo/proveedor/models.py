from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Proveedor(models.Model):
	user=models.OneToOneField(User)
	nombre=models.CharField(max_length=15,null=True,)
	fechaafiliacion=models.DateField(null=True,)
	rfc=models.CharField(max_length=10,null=True,)

	def __unicode__(self):
		return u'%s' % (self.user)

	def create_user_proveedor(sender, instance, created, **kwargs):
		if created:
			Proveedor.objects.create(user=instance)

	post_save.connect(create_user_proveedor, sender=User)

class Articulo(models.Model):
	nombre=models.CharField(max_length=15,)
	preciocompra=models.IntegerField()
	precioventa=models.IntegerField()
	cantidadexistente=models.IntegerField()
	proveedor=models.ForeignKey(Proveedor)

	def __unicode__(self):
		return u'%s' % (self.nombre)

class Tienda(models.Model):
	
	nombre=models.CharField(max_length=20,)
	fechainauguracion=models.DateField(auto_now_add=True)
	articulos=models.ManyToManyField(Articulo)
	proveedores=models.ManyToManyField(Proveedor)
	empleados=models.ManyToManyField(User)

	def __unicode__(self):
		return u'%s' % (self.nombre)