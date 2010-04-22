from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from mrben.main.models import Entry, Category



def index(request):
	""" Homepage view. Displays a list of blogs posts. """
	# TODO: Pagination.
	entry_list = Entry.objects.published().order_by('-publish')
	return render_to_response('home.html', {
	    'entry_list': entry_list,
	    'project': None,
	    'link_list': None,
	    'show_comments': False,
	    }, context_instance=RequestContext(request))

def entry_detail(request, object_id=None, slug=None):
	""" Displays a single blog post with comments (if enabled). """
	try:
		if object_id:
			entry = Entry.objects.get(id=object_id)
		else:
			entry = Entry.objects.get(slug=slug)
	except Entry.DoesNotExist:
		entry = None
	
	return render_to_response('entry_detail.html', {
	    'entry': entry,
	    'show_comments': True,
	    }, context_instance=RequestContext(request))

def category_list(request):
	""" Lists all categories with links to blog entry lists. """
	category_list = Category.objects.all().order_by('title')
	return render_to_response('category_list.html', {
	    'category_list': category_list,
	    }, context_instance=RequestContext(request))

def category_detail(request, title):
	""" Lists all blog posts in a particular category. """
	entry_list = Entry.objects.published().filter(categories__title=title)
	return render_to_response('category_detail.html', {
	    'entry_list': entry_list,
	    'category_title': title,
	    'show_comments': False,
	    }, context_instance=RequestContext(request))

def _get_featured_project():
	""" Get a blog entry suitable for a feature box. """
	try:
		entry = Entry.objects.published().filter(categories__title__in=['Projects','Portfolio']).order_by('?')[0]
		return entry
	except Entry.DoesNotExist:
		pass
	except IndexError:
		pass
	
	return
