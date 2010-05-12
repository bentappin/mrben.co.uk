from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings

from mrben.main.models import Entry, Category


def index(request):
	""" Homepage view. Displays a list of blogs posts. """
	entry_list = (Entry.objects.published().exclude(categories__title='Projects')
	                .exclude(categories__title='Portfolio').order_by('-publish'))
	return _paginated_entry_list(request, 'Some of my news', entry_list)

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

def category_detail(request, category_slug):
	""" Lists all blog posts in a particular category. """
	category = get_object_or_404(Category, slug=category_slug)
	entry_list = Entry.objects.published().filter(categories__slug=category_slug)
	return _paginated_entry_list(request, category.title, entry_list)

def _paginated_entry_list(request, title, entry_list):
	""" Generic view for displaying paginated lists of Entry instances. """
	paginator = Paginator(entry_list, settings.ENTRIES_PER_PAGE)
	
	# See if a specific page is required, if not default to first.
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

	# Grab paginated set. If request page is out of range, show last page.
	try:
		entries = paginator.page(page)
	except (EmptyPage, InvalidPage):
		entries = paginator.page(paginator.num_pages)
	
	return render_to_response('entry_list.html', {
	    'title': title,
	    'entries': entries,
	    'project': None,
	    'link_list': None,
	    'show_comments': False,
	    }, context_instance=RequestContext(request))

def _get_featured_project():
	""" Get a blog entry suitable for a feature box. """
	try:
		entry = Entry.objects.published().filter(categories__slug__in=['projects','portfolio']).order_by('?')[0]
		return entry
	except (Entry.DoesNotExist, IndexError):
		pass
	return
