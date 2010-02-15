from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from mrben.main.models import *
from mrben.main.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Setup variables for generic views
def get_featured_project():
	queryset = Entry.objects.published().filter(categories__title__in=['Projects','Portfolio']).order_by('?')
	if queryset:
		return queryset[0]
	
def get_links():
	return Link.objects.all()

entry_info = {
	'queryset': Entry.objects.published(),
	'template_name': 'entry_detail.html',
	'template_object_name': 'entry',
}

home_page_info = {
	'queryset': Entry.objects.published().exclude(categories__title='Projects').exclude(categories__title='Portfolio'),
	'template_name': 'home.html',
	'template_object_name': 'entry',
	'extra_context': { 	'project': get_featured_project,
	 					'link_list': get_links }
}

projects_info = {
	'queryset': Entry.objects.published().filter(categories__title='Projects'),
	'template_name': 'projects.html',
	'template_object_name': 'project',
}

portfolio_info = {
	'queryset': Entry.objects.published().filter(categories__title='Portfolio'),
	'template_name': 'portfolio.html',
	'template_object_name': 'portfolio',
}

categories_info = {
	'queryset': Category.objects.all(),
	'template_name': 'category_list.html',
	'template_object_name': 'category',
}

category_info = {
	'queryset': Entry.objects.published(),
	'template_name': 'category_detail.html',
	'template_object_name': 'entry',
}


# URL patterns
urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),

	# Front page
	(r'^$', list_detail.object_list, home_page_info),

	# Pages
	#(r'^about/$',direct_to_template, {'template': 'about.html'}),
	(r'^projects/$', list_detail.object_list, projects_info),
	(r'^portfolio/$', list_detail.object_list, portfolio_info),
	(r'^categories/$', list_detail.object_list, categories_info),
	(r'^category/(?P<title>[-\w]+)/$', category_detail),
	
	# "Blog" pages
	(r'^(entry|project|portfolio)/(?P<object_id>\d+)/$', list_detail.object_detail, entry_info),
	
	(r'^comments/', include('django.contrib.comments.urls')),
)

if settings.DEBUG == True:
	urlpatterns += patterns('',
		# Dev static files
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}),
	)