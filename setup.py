from setuptools import setup, find_packages

setup(

	name = "ListenIO", 
	version = "0.1", 
	packages = find_packages(), 
	scripts = 'Main.py', 
	installrequires = ['youtube-dl>=2014.05.12', 'ffmpeg>=2.2' , 'lame>=3.99' , 'beautifulsoup>=4.3' , 'gdata>=1.0'], 
	author = 'Shantanu Srivastava', 
	author_email = 'shantanu1002@gmail.com' , 
	license = 'BSD'
	
	)