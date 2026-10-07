import os
import shutil
import glob
from PIL import Image, ImageOps

# Please change the input_dir folder to your folder containing the photos your wanting to have edited.
# Please change the output_dir folder to your folder you want the edited photos to appear in.

input_dir = r"C:\Users\MrUser\Pictures\Practice"                   # The folder containing photos that need corrected.  Folder path should be a raw string like r"C:\Users\MrUser\Pictures\Practice".
output_dir = r"C:\Users\MrUser\Pictures\Practice2"                   # The folder that the corrected photos will go into after being passed through the script.  Folder path should also be a raw string.

with os.scandir(input_dir) as target_dir:                   # Gets the folder containing the photos to be corrected and gets the files ready to be passed through the script.
    for entry in target_dir:
        if entry.name.endswith(".jpg") and entry.is_file():                 # Checks if file is a jpeg and if it's a file.
            x = entry.path                  # If the file is a file and is a jpeg, it gets stored in a variable.
            y = Image.open(x)                   # Opens the image file and stores it in a variable.
            y = ImageOps.exif_transpose(y)                  # Changes the orientation of the image in the file to orientation: 1.
            y.save(entry.path + 'imageops-exif_transpose.jpg')                  # Saves the file with the file path changed to reflect that it's been passed through the script.
        if entry.name.endswith(".mp4") and entry.is_file():                 # Checks if file is an mp4 and if it's a file.
            shutil.move(entry, output_dir)                  # Moves mp4 files to the new folder where the corrected photos go.
            print('Moved:', entry)                  # Returns a message letting the user know that the mp4 files have been moved to the folder that contains the corrected photos.

pattern = '\*.jpgimageops-exif_transpose.jpg'                   # This is what is added to the end of the file paths to easily identify which files have been passed through the script.
picts = glob.glob(input_dir + pattern)                  # Stores the jpeg files with altered path names in a variable.

for pic in picts:
    shutil.move(pic, output_dir)                    # Moves each jpeg file into the folder for the corrected photos.
    print('Moved:', pic)                    # Returns a message for each file that is moved into the folder for storing the corrected photos.
