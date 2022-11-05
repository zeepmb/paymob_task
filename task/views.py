import os
import pandas as pd

from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from throttle.decorators import throttle
from task import result


class HomeView(TemplateView):
    """
    A class for home view.

    Methods
    -------
    get (request):
        Returns a html view with data
    """

    template_name = 'home.html'

    @method_decorator(throttle(zone='default'))
    def get(self, request):
        """
        Return an HttpResponse whose content is filled with the result of calling
        django.template.loader.render_to_string() with the passed arguments.

        Parameters
        ----------
        request : django request
            Key value to be matched with values

        Returns
        -------
        renderer : HttpResponse
            Html Renderer with context
        """
        a = result.get_key_values()
        context = {
            'keys': a['key'],
        }
        return render(request, self.template_name, context)


class ResultView(TemplateView):
    """
        A class to represent filter view.

        Attributes
        ----------
        template_name : str
            template used for this view

        Methods
        -------
        post(request):
            Returns a html renderer with context
        """

    template_name = 'result.html'

    @method_decorator(throttle(zone='default'))
    def post(self, request):
        """
        Return an HttpResponse whose content is filled with the result of calling
        django.template.loader.render_to_string() with the passed arguments.

        Parameters
        ----------
        request : django request
            Key value to be matched with values

        Returns
        -------
        renderer : HttpResponse
            Html Renderer with context
        """

        selected_key = request.POST.get('keys', '')
        filtered = result.get_matching(selected_key)
        context = {
            'selected_key': selected_key,
            'filtered': filtered
        }
        return render(request, self.template_name, context)
