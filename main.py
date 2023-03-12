import os
import random
import ctypes

# set the path to the folder where the images are stored
folder_path = "C:\\Users\\YourUserName\\Pictures\\Desktop Backgrounds"

# get a list of all the image file names in the folder
images = os.listdir(folder_path)

# choose a random image from the list
image_path = os.path.join(folder_path, random.choice(images))

# set the chosen image as the desktop background
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
