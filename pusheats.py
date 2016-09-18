#! /usr/bin/python

from flask import Flask, request, send_file
import random
import urllib
from PIL import ImageFile

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/_get_pusheen')
def get_pusheen():
	# Sad pusheen
	if request.args.get('type') == '0':
		filename = "sad_pusheen.png"
	# Neutral pusheen
	elif request.args.get('type') == '1':
		filename = "neutral_pusheen.png"
	# Happy pusheen
	elif request.args.get('type') == '2':
		filename = "happy_pusheen.png"
	else:
		filename = "happy_pusheen.png"
	return send_file(filename, mimetype="image/png")

# Given data structure with urls to xkcd images, return a random one as a JSON 
# object
@app.route('/_get_xkcd')
def get_xkcd():
	# Fake array
	img_arr = ["https://imgs.xkcd.com/comics/stove_ownership.png"]
	# Get random index	
	index = random.randint(0, len(img_arr) - 1)
	url = img_arr[index]

	open_file = urllib.urlopen(url)
	parser = ImageFile.Parser()
	data = open_file.read(1024)
	if not data:
		return
	parser.feed(data)
	if parser.image:
		return parser.image 


if __name__ == '__main__':
    app.run()

