'''
Created on May 30, 2014

This is a decorator which, when applied to a view, allows only users who have edit permissions on the requested object to view the object.

As it stands, I do no believe it is possible to write a decorator that has dynamic knowledge of objects within the view.
Instead, I have found the model from a parameter which can be passed to the decorator, so the model handled by a view is assumed to be known prior to runtime.

This is useful because now we can capture some object identifier from the urlconf and pass it as a view parameter to find the specific object.
I'm just assuming (for simplicity) that we are going to capture the primary key from the urlconf and use it in the view params.
Realistically, we could use any identifying information about the object to get the object.

Once we know a model (decorator params) and some identifying information for the object (passed to the view), we can check the object permissions.

There is one precondition which must be in place for this decorator to function correctly:
In order to check permissions on a per-object basis, the object model must include a many-to-many field which associates the object with which users are allowed to edit it.

@author: MRHardwick
'''

from django.db import models
from django.contrib.auth.models import User

import functools
from django.shortcuts import get_object_or_404
from django.http import Http404


class PerObjectPermissionModel(models.Model):
    '''A Model which retains a many-to-many relationship with the User model so that we can store per-object user permissions.
    '''
    users_with_change_access = models.ManyToManyField(User)
    # Add other permission lists as desired.



def can_edit_object(model):
    '''A decorator which will detect whether the object can be modified by the current user.
    
    @param model: The object model from which we will get the specific object instance.
    '''
    
    def decorator(view_function):
        '''The decorator itself.
        '''
        
        @functools.wraps(view_function)
        def decorator_wrapper(request, *args, **kwargs):
            
            # Get the primary key from the arguments passed from the urlconf.
            
            primary_key = kwargs.get('pk', None)
            
            # Raise a descriptive exception if the primary key is not provided.
            
            if primary_key is None:
                raise RuntimeError('Decorator requires a primary key be captured from the url in urlconf.')
            
            # Get an instance of this specific object.
            
            obj = get_object_or_404(model, pk=primary_key)
            
            # Is the current user associated with the object instance as having change permissions?
            
            if obj.users_with_change_access.filter(pk=request.user.pk).exists():
                
                # Allow them in.
                
                return view_function(request, *args, **kwargs)
                
            else:
                
                # They get a 404.
                
                raise Http404
            
        return decorator_wrapper
    
    return decorator