from django.db.models import Manager
import datetime

class PublicManager(Manager):
	"""Returns published posts that are not in the future."""
	def __init__(self, *args, **kwargs):
		self.filter_dict = dict(status=1, publish__lte=datetime.datetime.now())
		super(PublicManager, self).__init__(*args, **kwargs)
	
	def published(self):
		return self.get_query_set().filter(status=1, publish__lte=datetime.datetime.now())
		
