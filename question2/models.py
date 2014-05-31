'''
Created on May 30, 2014

@author: MRHardwick
'''

from django.db import models

class Campus(models.Model):
    '''
    
    '''
    
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    
    
class Student(models.Model):
    '''
    '''
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    campuses = models.ManyToManyField(Campus)
    main_campus = models.ForeignKey(Campus)