from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from django.contrib import admin
from django.http import HttpResponseRedirect

from mrben.main.views import index, entry_detail, category_detail, category_list
from mrben.main.feeds import EntriesFeed


admin.autodiscover()

# URL patterns
urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),

	# Front page
	(r'^$', index),

	# Pages
	(r'^categories/$', category_list),
	(r'^category/(?P<category_slug>[-\w]+)/$', category_detail),
	
	# "Blog" pages
	(r'^(entry|project|portfolio)/(?P<object_id>\d+)/$', entry_detail),
    (r'^(entry|project|portfolio)/(?P<slug>[-\w]+)/$', entry_detail),
    
	# Syndication feeds
	(r'^feed/$', EntriesFeed()),
	
	(r'^favicon\.ico$', lambda r: HttpResponseRedirect('/static/images/favicon.ico')),
)

if settings.DEBUG == True:
	urlpatterns += patterns('',
		# Dev static files
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}),
	)
