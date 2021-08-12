# Pull wikipedia article with 2-word title. 
# Check dictionary to make sure name is adjective + noun. 

import wikipedia
from PIL import Image, ImageFont, ImageDraw

# bad code
# write better code sometime
def get_sus_string():
	while True:
		# this is a workaround so that even if
		# only one word counts as a name, the whole title gets skipped.
		title_marked = False;

		with open("./names_big.txt", encoding="utf-8") as file:
			lines = file.read().splitlines()
		page_title = wikipedia.random(pages=1)
#		print("[tried pulling title]", page_title) # debug

		if page_title.count(" ") == 1:
#			print("[good wordcount]", page_title) # debug

			# break name into individual words
			words = page_title.split(" ")

			# check with dictionary to avoid half the sus memes being with names
			for word in words:
				if word in lines:
#					print("word is name, ", word) # debug
					title_marked = True;
					continue
				elif title_marked == False and '(' not in page_title: 
#					print("word is good, ", page_title) # debug
					sus_string = "When the", words[1].replace(',', '').lower(), "is", words[0].replace(',', '').lower()+"!"
					output = ' '.join(sus_string)
					if len(output) > 32:
						continue
					return output
					

# stolen from stackoverflow user tiwo 
# https://stackoverflow.com/questions/43730389/correctly-centring-text-pil-pillow
def center_text(img, font, text, color=(255, 255, 255)):
	strip_width, strip_height = 600, 100
	draw = ImageDraw.Draw(img)
	text_width, text_height = draw.textsize(text, font)
	position = ((strip_width-text_width)/2,(strip_height-text_height)/2)
	draw.text(position, text, color, font=font)
	return img


def render_images():
	counter = 0
	while counter <= 25: # set sus limit here. maybe move this to commandline arg?
		template = Image.open("jermasus_template.jpg")
		caption_font = ImageFont.truetype('calibri.ttf', 36)
		caption_text = get_sus_string()

	#	image_slate = ImageDraw.Draw(template)
	#	image_slate.text((25,25), caption_text, (0, 0, 0), font=caption_font)
		
		image_slate = center_text(template, caption_font, caption_text, color=(0, 0, 0))
		counter += 1
		template.save('outputs/sus_{}.jpg'.format(counter))


render_images()