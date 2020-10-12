""" Django models utilities. """

# Django 
from django.db import models

class CRideModel(models.Model):
    """ Comparte Ride base model 
    
    CRideModel acts as an abstract base class from which every
    other model in the project will in inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created
        + modified (DateTime): Store the last datetime the object was modified
    """ 
    created = models.DateTimeField(
        'created at', 
        auto_now_add=True, 
        help_text='Date time on which the object was created.'
    )

    modified = models.DateTimeField(
        'modified at', 
        auto_now=True, 
        help_text='Date time on which the object was modified.'
    )

    class Meta:
        """ Meta option. """
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified'] 

# Herencia Ejemplo
"""
class Student(CRideModel):
    name = models.CharField('', max_length=50)    

    class Meta(CRideModel.Meta):
        db_table = 'student_role'

class Person(models.Model):
    first_name = models.CharField('', max_length=50)
    last_name = models.CharField('', max_length=50)

class MyPerson(Person):
    class Meta:
        proxy = True
    
    def say_hi(name):
        pass

MyPerson.objects.all()
anthony = MyPerson.objects.get(pk=1)
anthony.say_hi('Anthony')

rulo = Person.objects.get(pk=2)
rulo.say_hi('Anthony')
"""