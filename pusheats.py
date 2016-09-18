#! /usr/bin/python

from flask import Flask, request, send_file
import random
import urllib
import os
import random
from PIL import ImageFile

app = Flask(__name__)

app.config['DEBUG'] = True
# Static pusheen resources
PUSHEEN_SOURCE = "assets/pusheen/"

# Static XKCD resources
XKCD_SOURCE = "assets/xkcd/"
VALID_XKCD = "Beer, contents, Dehydration, Delicious, Diet Coke+Mentos, Exercise, Food Combinations, Free, house_of_pancakes.png, Juicer, Learning to Cook, Lunch, Making Hash Browns, Meat Cereals, Michael Phelps, Recipes, RPS, Sandwich, Shake That, stove_ownership.png, To Taste, Yogurt".split(", ")

# Static text resources
POS_TEXT = [
    "Healthy foods, such as fruits, vegetables, and lean meats, can promote your overall health and protect against disease!",
    "Eating healthy foods reduces the likelihood of developing type 2 diabetes, heart disease, and cancer.",
    "Eating healthy foods can build a healthy heart and improve long-term cardiovascular functioning.",
    "Studies show a link between eating healthy foods and longer life expectancy.",
    "Veggies - such as lettuce and other leafy greens, broccoli, bok choy, cabbage, as well as garlic and onions - and fruits protect against many types of cancer.",
    "Fruits, vegetables, and lean meats are low in fat, calories, and cholesterol.",
    "Fruits, vegetables, and lean meats contain essential vitamins and minerals to help your body function.",
    "Eating more healthy foods is an important way to improve heart health, blood sugar levels, and longevity.",
    "Healthy foods have unique flavors and textures, and can be prepared in creative and delicious ways.", 
    "You can combine natural ingredients to make multiple flavors and textures to be part of a complex and interesting meal.", 
    "Fruit can be a juicy and sweet snack; berries are aromatic and earthy, watermelon is summery and juicy, and citrus is tangy and fresh.", 
    "Vegetables also have unique tastes and textures; carrots are sweet and crunchy, lettuce is fresh and light, avocado is smooth and creamy, and beets are sweet and earthy.", 
    "Lean meats, such as poultry and fish, can be flavorful and savory, especially when prepared with spices.", 
    "Research suggests that eating healthy foods you don't typically eat can increase both liking and strong desire for these foods; if you give broccoli a try, eventually you might crave it!", 
    "Eating healthy foods feels good physically. ",
    "The fiber in fruits and vegetables aids with digestion and slows the release of sugar into the bloodstream, improving energy levels, digestion and blood sugar regulation.", 
    "Vitamins and nutrients in fruits, vegetables, and lean meats can improve the health of your nails, hair, and teeth.",
    "Eating healthy foods, especially fish and lean poultry, can increase energy levels and build stronger bones and muscles, which helps improve athletic performance.", 
    "Research suggests that people who consume large amounts of fruits and vegetables develop more glowing and healthy-looking skin - and are perceived as more attractive.",
    "Eating healthy foods feels good emotionally.",
    "Eating healthy meals can improve mood by increasing self-esteem, both in the short-term and the long-term.", 
    "Vitamins and minerals in healthy foods can help improve mood.",
    "In addition, when people eat healthy food they report feeling proud of good food choices and happy about taking care of their health." 
    ]

NEG_TEXT = [
    "Eating unhealthy foods, especially foods high in fat, sugar, or salt, can have negative effects in the short-term and the long-term.", 
    "Eating unhealthy foods increases risk for obesity and associated health problems. ",
    "Obesity-related health conditions, associated with eating unhealthy foods, include heart disease, stroke, type 2 diabetes and certain types of cancer, some of the leading causes of preventable death.", 
    "Obesity also increases blood pressure, the leading cause of stroke, and can increase risk of diabetes.",
    "Type 2 diabetes, associated with the consumption of unhealthy foods, is a disease in which blood sugar levels are above normal, which can lead to heart disease, kidney disease, stroke, amputation, nervous system damage, erectile dysfunction, and blindness.",
    "Obesity has also been associated with various deadly forms of cancer, including cancer in the esophagus, pancreas, colon, breast, ovaries, kidney, thyroid, and gallbladder.",
    "Even if individuals are not overweight, diets high in fat, sugar, and salt have negative effects on health.",
    "Studies have found that eating red meat can increase risk of heart failure, and that a diet high in salt or sugar can increase risk of high blood pressure and heart disease.", 
    "Consuming salt and red meat can increase high blood pressure and risk of stroke.",
    "Large research studies, including one conducted at Harvard, have found that consumption of sugar and red meat increases risk of developing diabetes.", 
    "In a study with over 150,000 participants, diets high in fat, salt, and sugar all have been linked to increased risk of cancer.",
    "A major aspect of prevention and treatment for these health conditions is changing dietary habits, including eating fewer unhealthy foods and reducing consumption of fat, sugar, and salt.", 
    "Eating unhealthy foods feels bad physically.",
    "People who eat unhealthy foods high in fat, sugar, and salt report feeling very full and lethargic after meals.", 
    "Fat, sugar, or salt can slow digestion and cause rapid increases in blood sugar, causing stomach aches, mood swings, and sugar crashes.", 
    "Eating unhealthy foods can hurt athletic performance by failing to provide balanced nutrition, decreasing overall energy levels, and preventing the growth of stronger bones and muscles.", 
    "Eating an unhealthy meal can feel bad emotionally.",
    "People report feeling guilty, ashamed, and neglectful of their health immediately after consuming unhealthy foods.", 
    "In the long-term, eating unhealthy foods can worsen self-esteem, including about their appearance, lead people to believe that they lack self-control, and increase negative emotion surrounding health and weight.",
    "Research has found that poor eating habits can worsen a persons' mood and even increase the risk of developing clinical depression in the long-term."
    ]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_xkcd')
def get_xkcd():
    f_no = random.randint(0, len(VALID_XKCD) - 1)
    print VALID_XKCD, f_no
    return send_file(XKCD_SOURCE + VALID_XKCD[f_no], mimetype="image/png")

@app.route('/get_pusheen')
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
	return send_file(PUSHEEN_SOURCE + filename, mimetype="image/png")

@app.route('/get_text')
def get_text():
    if request.args.get('type') == '1':
         f_no = random.randint(0, len(POS_TEXT) - 1)
         return POS_TEXT[f_no]
    else:
        f_no = random.randint(0, len(NEG_TEXT) - 1)
        return NEG_TEXT[f_no]
   
# Given data structure with urls to xkcd images, return a random one as a JSON 
# object
#@app.route('/_get_xkcd')
#def get_xkcd():
#	# Fake array
#	img_arr = ["https://imgs.xkcd.com/comics/stove_ownership.png"]
#	# Get random index	
#	index = random.randint(0, len(img_arr) - 1)
#	url = img_arr[index]
#
#	open_file = urllib.urlopen(url)
#	parser = ImageFile.Parser()
#	data = open_file.read(1024)
#	if not data:
#		return
#	parser.feed(data)
#	if parser.image:
#		return parser.image 

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
