from PIL import Image, ImageSequence

# convert png to jpg
def png_to_jpg(png_path, jpg_path):
    im = Image.open(png_path)
    im = im.convert('RGB')
    im.save(jpg_path)

png_to_jpg('images/headshot_circle.png', 'images/headshot_circle.jpg')
