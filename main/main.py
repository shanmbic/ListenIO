# !/usr/bin/python

import bs4 as bp 
import urllib2
import re
import gdata.youtube
import gdata.youtube.service
import subprocess
import os
import pdb
import getpass

yt_service = gdata.youtube.service.YouTubeService()
yt_service.developer_key = 'AI39si7SAhwaCZoAs5QswjEL4TCbKeGAGFeeb2-M4zowLaJqe1uX4LWjWLf6d0y6pDiXIhD9EXVenMD-pFR_COQNxBAJGyiwaQ'

def SearchAndPrint(search_terms):
	yt_service = gdata.youtube.service.YouTubeService()
	query = gdata.youtube.service.YouTubeVideoQuery()
	query.vq = search_terms
	query.orderby = 'viewCount'
	query.racy = 'include'
	feed = yt_service.YouTubeQuery(query)
	x=feed.entry[2]
	return re.sub('&[\w\W]*', '' , x.media.player.url)

def process(search_terms):
	url=SearchAndPrint(search_terms)
	user = getpass.getuser()
	cwd = os.getcwd()
	out_dir = '/home/' + user + '/Music/'
	main_porc = subprocess.call(['youtube-dl','-o',"%(title)s.%(ext)s",url])
	proc = subprocess.Popen(['youtube-dl' , '-e' , '-o' ,"%(title)s.%(ext)s" , url] , stdout=subprocess.PIPE)
	filename = re.sub('\n','', proc.communicate()[0])
	filename = re.sub(r'"', r"'" , filename )
	#pdb.set_trace()
	os.rename(filename+".mp4","test.mp4")
	subprocess.call(['ffmpeg','-i','test.mp4', 'test.wav'])
	subprocess.call(['lame', 'test.wav', out_dir + filename + '.mp3'])
	os.remove('test.mp4')
	os.remove('test.wav')


url = urllib2.urlopen('http://www.vh1.com/shows/series/top_20_countdown/')
content = url.read()
song_dict=[]
with open('song.txt' , 'rw') as f:
	for line in f.readlines():
		artist , song = line.split("-")
		song_dict.append( artist + '-' + re.sub('\n','',song))


soup = bp.BeautifulSoup(content)
soup_song = soup.select('span.song')
soup_artist = soup.select('span.artist')

for i in range(0,20):
	detail = soup_artist[i].text + '-' + soup_song[i].text
	if detail in song_dict:
		continue
	else:
		song_dict.append(detail)
		process(detail)


string=''

for key in song_dict:
	string = string + key + '\n'
	
with open('song.txt' , 'w') as f:
	f.write(string)




