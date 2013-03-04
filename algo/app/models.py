from django.db import models

class Curso(models.Model):
	clave=models.CharField(max_length=5)
	nombre=models.CharField(max_length=30)
	costo=models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.nombre)


class Campus(models.Model):
	nombre=models.CharField(max_length=30)
	direccion=models.TextField()
	email=models.EmailField(max_length=25)
	cursos=models.ManyToManyField(Curso)

	def __unicode__(self):
		return u'%s' % (self.nombre)


class Alumno(models.Model):
	nombre=models.CharField(max_length=30)
	matricula=models.IntegerField()
	campus=models.ForeignKey(Campus)
	cursos=models.ManyToManyField(Curso)

	def __unicode__(self):
		return u'%s' % (self.nombre)



