'''
Created on May 30, 2014

This is an example of a class-based view that uses the django authorization decorator login_required.
This view responds to GET and POST requests with a simple json body indicated an 'OK' status.

Demonstrates the use of a so-called mixin for django class-based views.

@author: MRHardwick
'''

from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json

class LoginRequiredMixin(object):
    '''A simple wrapper that allows the class-based view to do authorization checks through the django authorization decorator login_required.
    '''
    
    @classmethod
    def as_view(cls, **initkwargs):
        '''Overrides the as_view method which will be used when the class-based view is mapped to a urlconf.
        '''
        
        # Get a copy of the underlying/wrapped view.
        
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        
        # Run the view through the authorization decorator.
        
        return login_required(view)



class HealthCheckView(LoginRequiredMixin, View):
    '''A class-based view which returns a response to GET and POST requests with a simple json body.
    '''

    def get(self, request, *args, **kwargs):
        '''Responds to requests made by the GET method with a simple json status message.
        '''
        return HttpResponse(json.dumps({"status": "OK"}), mimetype = 'application/json')
        
    def post(self, request, *args, **kwargs):
        '''Responds to requests made by the POST method with a simple json status message.
        '''
        return HttpResponse(json.dumps({"status": "OK"}), mimetype = 'application/json')