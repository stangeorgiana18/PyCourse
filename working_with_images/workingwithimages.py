# pillow library is a fork of PIL library

from PIL import Image

mac = Image.open('example.jpg')
print(type(mac)) # <class 'PIL.JpegImagePlugin.JpegImageFile'>

#mac.show()

print(mac.size) # (1993, 1257) -- (width, height)
print(mac.filename)
print(mac.format_description) # JPEG (ISO 10918)

# CROPPING IMAGES 
mac.crop((0,0, 100, 100)).show()

pencils = Image.open('pencils.jpg')
print(pencils.size) # (1950, 1300)

# grab the top pencils from the picture
x = 0
y = 0

# 30% in the x direction
# 10% in the y direction
w = 1905 / 3 # width
h = 1300 / 10

pencils.crop((x, y, w, h)).show()

# start point: (x, y)

# BOTTOM PENCILS
x = 0
y = 1100 # y starts at 1100

w = 1950 / 3
h = 1300

pencils.crop((x, y, w, h)).show()

# grab the computer itself from the mac photo

halfway = 1993 / 2
x = halfway - 200 # halfways - 200 pixels
w = halfway + 200 

y = 800
h = 1257

mac.crop((x, y, w, h)).show()


# CREATE A COPY to the top left corner
computer = mac.crop((x, y, w, h))
mac.paste(im = computer, box = (0, 0)) # (what to go, where)

mac.show()

mac.paste(im = computer, box = (796, 0)) 
#mac.show() # the variable is permanently affected, but not the image


mac.resize((3000, 500)).show()


# rotate the image by 90 degrees
mac.rotate(90).show()

print('\n')


# COLOR TRANSPARENCY

# RGBA - red, green, blue, alpha -- 0-255
# if alpha = 0 --> image is completely transparent
# alpha = 255 --> image completely opaque

red = Image.open('red_color.jpg')
blue = Image.open("blue_color.png").convert('RGB')


# reset the alpha 
blue.putalpha(100)
#blue.show()

red.putalpha(100)
#red.show()
#print("Alpha:", red.getchannel('A'))

blue.paste(im = red, box = (0, 0), mask = red) # the mask should be the same as the image
#blue.show()

blue.save("purple.png")
purple = Image.open("purple.png")
#purple.show()



# IMAGE EXERCISE

# stack images on top of each other, work with transparency, resizing images
words = Image.open('word_matrix.png')
mask = Image.open('mask.png')

print(words.size) # (1015, 559)
print(mask.size) # (505, 251)

# enlarge the mask to the size of the word matrix
mask = mask.resize((1015, 559))
print(mask.size)

mask.putalpha(150)
#mask.show()

words.paste(im = mask, box = (0, 0), mask = mask)
words.save("secret_words.png")
secret_words = Image.open('secret_words.png')
secret_words.show()

