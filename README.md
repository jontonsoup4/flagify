#What is flagify?
`flagify` combines a local image or image url with a picture of a flag. Modeled after the Facebook profile support image, this module expands the functionality to take input from a url (such as a Facebook profile picture) or a local image and combine it with a flag of the user’s choice.

# Example script
‘’’
from flagify import Flagify

# takes an image's url as an argument, adds url=True, combines the image with flags.png, and saves it
image_url = 'https://raw.githubusercontent.com/jontonsoup4/flagify/master/examples/cat.jpg'
image = Flagify(image_url, url=True).add_flag('flags.png')
image.save('catflag.png')

# takes a local image, defaults to .jpg, combines the image with flags.png, and saves it
profile_picture = Flagify('melody').add_flag('flags.png')
profile_picture.save('melodyflags.png')
‘’’

##Rendered Picture
![Picture](https://github.com/jontonsoup4/ascii_art/blob/master/examples/catflags.png)


#Setup
`python3 setup.py install`

#Dependencies
`Pillow>=3.0.0`
