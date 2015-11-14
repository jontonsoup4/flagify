from flagify import Flagify

# takes an image's url as an argument, adds url=True, combines the image with flags.png, and saves it
image_url = 'https://raw.githubusercontent.com/jontonsoup4/flagify/master/examples/cat.jpg'
image = Flagify(image_url, url=True).add_flag('flags.png')
image.save('catflag.png')

# takes a local image, defaults to .jpg, combines the image with flags.png, and saves it
profile_picture = Flagify('melody').add_flag('flags.png')
profile_picture.save('melodyflags.png')