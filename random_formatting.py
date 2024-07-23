# reformat this image to be 300px by 300px

from PIL import Image

image = r"C:\Users\flow\PycharmProjects\andrewsheerin.github.io\images\storymap.png"
img = Image.open(image)
img = img.resize((300, 300))

# overlay image/img.png on top of image
img2 = r"C:\Users\flow\PycharmProjects\andrewsheerin.github.io\images\img.png"
img2 = Image.open(img2)
img.paste(img2, (0, 0))


img.save(r"C:\Users\flow\PycharmProjects\andrewsheerin.github.io\images\storymap_300.png")

