import os, random
from datetime import datetime

from django.conf import settings
from django.core.cache import cache

import twitter, pylast, flickrapi, random


def features(request):
	random.seed()
	prefix_path = 'includes/secondary'
	
	choices = []
	for template_dir in settings.TEMPLATE_DIRS:
		path = os.path.join(template_dir, prefix_path)
		for f in os.listdir(path):			
			choices.append(os.path.join(prefix_path, f))
	
	features = []
	used_indexes = []
	c_max = len(choices)
	for i in range(settings.FEATURE_SIDEBAR_COUNT):
		if len(used_indexes)==0:
			index = random.randrange(0, c_max)
		
		while index in used_indexes:
			index = random.randrange(0, c_max)
			
		used_indexes.append(index)
		features.append(choices[index])
	
	return {'features': features}

def latest_tweets(request):
	tweets = cache.get('tweets')

	if tweets is None:
		try:
			tweets = twitter.Api().GetUserTimeline(settings.TWITTER_USER, )[:5]
			for tweet in tweets:
				tweet.date= datetime.strptime( tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
				
			cache.set( 'tweets', tweets, settings.TWITTER_CACHE_TIMEOUT )
		except:
			tweets = None
	
	return {'tweets': tweets}

def latest_lastfm_tracks(request):
	tracks = cache.get('tracks')
	
	if tracks is None:
		try:
			network = (pylast.get_lastfm_network(api_key = settings.LASTFM_KEY,
				        api_secret = settings.LASTFM_SECRET, username = settings.LASTFM_USER,
				        password_hash = settings.LASTFM_PWDHASH))
			user = pylast.User('mrben_', network)
			if user.get_recent_tracks() > 4:
				tracks = user.get_recent_tracks()[:5]
			else:
				tracks = user.get_recent_tracks()[:len(user.get_recent_tracks())]
			
			cache.set( 'tracks', tracks, settings.LASTFM_CACHE_TIMEOUT )
		except:
			tracks = None
	
	return {'tracks': tracks}

def random_flickr_picture(request):
	picture = cache.get('picture')
	
	if picture is None:
		try:
			flickr = flickrapi.FlickrAPI(settings.FLICKR_KEY)
			photos = flickr.photos_search(user_id=settings.FLICKR_ID)
		
			total_pictures = photos.find('photos').attrib['total']
		
			pic_index = random.randint(0, int(total_pictures)-1)
		
			picture_id = photos.find('photos')[pic_index].attrib['id']
			server_id = photos.find('photos')[pic_index].attrib['server']
			farm_id = photos.find('photos')[pic_index].attrib['farm']
			secret = photos.find('photos')[pic_index].attrib['secret']
			
			image_url = "http://farm%s.static.flickr.com/%s/%s_%s_m.jpg" % (farm_id, server_id, picture_id, secret) 
			flickr_url = "http://www.flickr.com/photos/%s/%s" % (settings.FLICKR_ID, picture_id)
			
			picture = {'src': image_url, 'href': flickr_url}
			
			cache.set( 'picture', picture, settings.FLICKR_CACHE_TIMEOUT)
		except:
			picture = None
	
	return {'picture': picture}
	