from django.contrib import admin
from django import forms
from mrben.main.models import Entry, Category, Link

class EntryAdminForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EntryAdminForm, self).__init__(*args, **kwargs)
	
	body = forms.CharField(required=False,
												widget=forms.Textarea(attrs={
																'class': 'tinymce vLargeTextField'}))
	teaser = forms.CharField(	required=False,
														widget=forms.Textarea(attrs={
																		'class': 'tinymce vLargeTextField'}))
		
	class Meta:
		model = Entry
		
class EntryAdmin(admin.ModelAdmin):
	form = EntryAdminForm
	
	class Media:
		js = ('js/jquery/jquery-1.4.1.min.js',
					'js/tiny_mce/jquery.tinymce.js',
					'js/admin/entry.js',)
	

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category)
admin.site.register(Link)
