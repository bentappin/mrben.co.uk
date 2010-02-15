from datetime import datetime
from django.conf import settings
from django.core.cache import cache
import twitter, pylast, flickrapi, random

def latest_tweet(request):
	tweet = cache.get('tweet')
	
	if tweet:
		return {'tweet': tweet}
	
	try:	
		tweet = twitter.Api().GetUserTimeline(settings.TWITTER_USER, )[0]
		tweet.date= datetime.strptime( tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
		cache.set( 'tweet', tweet, settings.TWITTER_TIMEOUT )
	except:
		return {"tweet": None }
	
	return {"tweet": tweet}

def latest_tweets(request):
	tweets = cache.get('tweets')
	
	if tweets:
		return {'tweets': tweets}
	
	try:
		tweets = twitter.Api().GetUserTimeline(settings.TWITTER_USER, )[:5]
		for tweet in tweets:
			tweet.date= datetime.strptime( tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
	except:
		return {"tweets": None }
		
	cache.set( 'tweets', tweets, settings.TWITTER_TIMEOUT )
	
	return {"tweets": tweets}

def latest_lastfm_track(request):
	track = cache.get('track')
	
	if track:
		return {'track': track}
	
	try:
		network = (pylast.get_lastfm_network(api_key = settings.LASTFM_KEY,
					api_secret = settings.LASTFM_SECRET, username = settings.LASTFM_USER,
					password_hash = settings.LASTFM_PWDHASH))
		user = pylast.User(settings.LASTFM_USER, network)
		track = user.get_recent_tracks()[0]
	except:
		return {"track": None }
	
	cache.set( 'track', track, settings.LASTFM_TIMEOUT )
	
	return { 'track': track}

def latest_lastfm_tracks(request):
	tracks = cache.get('tracks')
	
	if tracks:
		return {'tracks': tracks}
	
	try:
		network = (pylast.get_lastfm_network(api_key = settings.LASTFM_KEY,
					api_secret = settings.LASTFM_SECRET, username = settings.LASTFM_USER,
					password_hash = settings.LASTFM_PWDHASH))
		user = pylast.User('mrben_', network)
		tracks = user.get_recent_tracks()[:5]
	except:
		return {"tracks": None }
	
	cache.set( 'tracks', tracks, settings.LASTFM_TIMEOUT )
	
	return {'tracks': tracks}

def random_flickr_picture(request):
	picture = cache.get('picture')
	
	if picture:
		return {'picture': picture}
	
	try:
		flickr = flickrapi.FlickrAPI(settings.FLICKR_KEY)
		photos = flickr.photos_search(user_id=settings.FLICKR_ID)
	
		total_pictures = photos.find('photos').attrib['total']
	
		pic_index = random.randint(0, int(total_pictures)-1)
	
		picture_id = photos.find('photos')[pic_index].attrib['id']
		server_id = photos.find('photos')[pic_index].attrib['server']
		farm_id = photos.find('photos')[pic_index].attrib['farm']
		secret = photos.find('photos')[pic_index].attrib['secret']
	except:
		return {"picture": None }
	
	image_url = "http://farm%s.static.flickr.com/%s/%s_%s_m.jpg" % (farm_id, server_id, picture_id, secret) 
	flickr_url = "http://www.flickr.com/photos/%s/%s" % (settings.FLICKR_ID, picture_id)
	
	picture = {'src': image_url, 'href': flickr_url}
	
	cache.set( 'picture', picture, settings.FLICKR_TIMEOUT)
	
	return {'picture': picture}
	