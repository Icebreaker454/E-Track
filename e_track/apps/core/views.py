"""
	Views for the home app

	Copyright by Icebreaker, 2015
"""

from django.views.generic import TemplateView


class Home(TemplateView):
	"""
	The view class for the home page
	"""
	template_name = 'core/landing.html'  