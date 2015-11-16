"""
	The url configuration for the base app

	Copyright by Icebreaker, 2015
"""

from django.conf.urls import url
from e_track.apps.core.views import Home

urlpatterns = [
	url(r'^$', Home.as_view(), name='home')
]