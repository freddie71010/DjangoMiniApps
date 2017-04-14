from django.conf.urls import url
from polls.views import *

app_name = 'polls'

# Generic template URLs
# ================================================================================
urlpatterns = [
	# ex: /polls/
	url(r'^$', IndexView.as_view(), name='index'),
	
	# ex: /polls/5/
	url(r'^specifics/(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
	
	# ex: /polls/5/results/
	url(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
	
	# ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
]
# ================================================================================


# Custom URLs
# ================================================================================
# urlpatterns = [
# 	# ex: /polls/
# 	url(r'^$', views.index, name='index'),
	
# 	# ex: /polls/5/
# 	url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	
# 	# ex: /polls/5/results/
# 	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	
# 	# ex: /polls/5/vote/
# 	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]
# ================================================================================
