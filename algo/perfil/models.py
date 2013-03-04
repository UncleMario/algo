from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

estadosciviles=(
	('S','Soltero'),
	('C','Casado'),
	('D','Divorciado'),
	('U','Union libre'),
	)

class Perfil(models.Model):
	user=models.OneToOneField(User)
	fechanacimiento=models.DateField(null=True,)
	domicilio=models.TextField(null=True)
	estadocivil=models.CharField(null=True, max_length=10, choices=estadosciviles,)
	friends=models.ManyToManyField(User,related_name='amigos')

	def __unicode__(self):
		return u'%s' % (self.user)

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Perfil.objects.create(user=instance)

	post_save.connect(create_user_profile, sender=User)

class Transaccion(models.Model):
	dueno=models.ForeignKey(User)
	fecha=models.DateField(auto_now_add=True,)
	cantidad=models.IntegerField()
	articulo=models.CharField(max_length=15,)

	def __unicode__(self):
		return u'%s' % (self.dueno)
