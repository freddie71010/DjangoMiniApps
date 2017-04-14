from django.conf.urls import url
from todos.views import *

app_name = 'todos'

# Generic template URLs
# ================================================================================
urlpatterns = [
	# ex: /todos/
	url(r'^$', IndexView.as_view(), name='index'),
]
