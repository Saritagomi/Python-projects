from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"C:\Users\hp\Pictures\WhatsApp Image 2023-01-08 at 12.18.05.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = 155
top = 134
right = 1539
bottom = 1343

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
newsize = (1700, 1700)
im1 = im1.resize(newsize)
# Shows the image in image viewer
im1.show()
