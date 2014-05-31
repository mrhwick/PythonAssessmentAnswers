'''
Created on May 30, 2014

This is a decorator which, when applied to a view, allows only users who have edit permissions on the requested model to view the object.
Detecting permissions by model is fairly simple.
We just need to check on our request user whether they have the permission '<app_name>.change_<model_classname>'.

If they don't have permissions, we'll send them to 404.
If they do have permissions, we'll pass them through to the view.

@author: MRHardwick
'''

import functools
from django.http import Http404



def can_edit_object(model):
    '''A decorator which will detect whether the given model can be modified by the current user.
    
    @param model: The object model which we are checking permissions over.
    '''
    
    def decorator(view_function):
        '''The decorator itself.
        '''
        
        @functools.wraps(view_function)
        def decorator_wrapper(request, *args, **kwargs):
            
            # Is the current user granted change permissions over this model type?
            
            if request.user.has_perm('<APP-NAME>.change_' + model.__name__.lower()):
                
                # Allow them in.
                
                return view_function(request, *args, **kwargs)
                
            else:
                
                # They get a 404.
                
                raise Http404
            
        return decorator_wrapper
    
    return decorator