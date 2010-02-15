from django.shortcuts import render_to_response
from django.http import HttpResponse
from mrben.main.models import Entry

def category_detail(request, title):
	entry_list = Entry.objects.published().filter(categories__title=title)
	return render_to_response('category_detail.html', { 'entry_list': entry_list,
																											'category_title': title })