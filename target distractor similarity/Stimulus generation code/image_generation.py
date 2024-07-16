import random
from PIL import Image
import numpy as np

# Define a function to return the centre coordinates of images given the grid codes
def get_coordinates(grid_loc,cell_size=125, jitter=37):
    # Switch case to return the centre coordinates of the images
    switcher = {
        1: (62.5, 687.5),
        2: (187.5, 687.5),
        3: (312.5, 687.5),
        4: (62.5, 562.5),
        5: (187.5, 562.5),
        6: (312.5, 562.5),
        7: (62.5, 437.5),
        8: (187.5, 437.5),
        9: (312.5, 437.5),
        10: (437.5, 687.5),
        11: (562.5, 687.5),
        12: (687.5, 687.5),
        13: (437.5, 562.5),
        14: (562.5, 562.5),
        15: (687.5, 562.5),
        16: (437.5, 437.5),
        17: (562.5, 437.5),
        18: (687.5, 437.5),
        19: (62.5, 312.5),
        20: (187.5, 312.5),
        21: (312.5, 312.5),
        22: (62.5, 187.5),
        23: (187.5, 187.5),
        24: (312.5, 187.5),
        25: (62.5, 62.5),
        26: (187.5, 62.5),
        27: (312.5, 62.5),
        28: (437.5, 312.5),
        29: (562.5, 312.5),
        30: (687.5, 312.5),
        31: (437.5, 187.5),
        32: (562.5, 187.5),
        33: (687.5, 187.5),
        34: (437.5, 62.5),
        35: (562.5, 62.5),
        36: (687.5, 62.5),
    }

    # Return the centre coordinates of the image
    (x,y)= switcher.get(grid_loc, "Invalid grid location")
    x=round(x-15+random.randint(-jitter,jitter))
    y=round(y+15+random.randint(-jitter,jitter))

    return (x,y)


# Paths to base images
base_images = {
    0: './black.jpg',
    1: './redLtri.jpg',
    2: './redRtri.jpg',
    3: './bcircle.jpg',
    4: './yLtri.jpg',
    5: './yRtri.jpg',
    6: './odiamond.jpg',
}


# Read tar_dis_locations.csv
import pandas as pd
df = pd.read_csv('locations.csv')

df = df.iloc[:10]


# Load base images
base_imgs = {code: Image.open(path) for code, path in base_images.items()}

# Resize base images to 30*30
for code, img in base_imgs.items():
    base_imgs[code] = img.resize((30, 30))
    #print size of each image
    #print(base_imgs[code].size)

# Make base images RGB and compatible with the stimulus image
for code, img in base_imgs.items():
    base_imgs[code] = img.convert('RGB')

import shutil
import os

# Delete gt, stimuli and target directories if they exist
if os.path.exists('gt'):  
    shutil.rmtree('gt')
if os.path.exists('stimuli'):
    shutil.rmtree('stimuli')
if os.path.exists('target'):
    shutil.rmtree('target')    

# Make new directories 
os.mkdir('gt')
os.mkdir('stimuli')
os.mkdir('target')


n=1

# Iterate along the rows of the dataframe
for index, row in df.iterrows():

    # Convert the row a df to numpy array
    temp_row = row.to_numpy()
    #print(temp_row)
    loc_rows=temp_row[0:35]
    target_index = np.where((loc_rows == 1) | (loc_rows == 2))[0][0]
    #print(target_index) 


    # Create a 750*750 image with a black background
    stimulus_image = Image.new('RGB', (750, 750), 'black')

    # Create white mask image
    mask = Image.new('RGB', (30, 30), 'white')
    
    # Paste base images into the grid with jitter and offsets
    for i in range(36):
        x, y = get_coordinates(i+1)
        img = base_imgs[row[i]]
        stimulus_image.paste(img, (x, y))
        
    # Create nessecery images
    mask_image = Image.new('RGB', (750, 750), 'black')

    # Create white mask image
    mask = Image.new('RGB', (30, 30), 'white')

    img=base_imgs[row[target_index]]
    x,y=get_coordinates(target_index+1)

    mask_image.paste(mask, (x, y))
    target=img

    # Save the image in the respective directories
    stimulus_image.save(f'stimuli/{n}.jpg')
    mask_image.save(f'gt/{n}.jpg')
    target.save(f'target/{n}.jpg')

    n=n+1

