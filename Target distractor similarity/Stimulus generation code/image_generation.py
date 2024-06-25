import random
from PIL import Image

# Paths to base images
base_images = {
    0: './black.png',
    1: './left_red_triangle.png',
    2: './right_red_triangle.png',
    3: './blue_circle.png',
    4: './left_yellow_triangle.png',
    5: './right_yellow_triangle.png',
    6: './orange_diamond.png'
}

# Load base images
base_imgs = {code: Image.open(path) for code, path in base_images.items()}

def create_stimulus_image(grid_codes, output_path, jitter_amount=5):
    # Size of each cell and the grid
    cell_size = 40
    grid_size = 6
    stimulus_size = cell_size * grid_size
    
    # Create a blank canvas for the stimulus image
    stimulus_image = Image.new('RGB', (stimulus_size, stimulus_size))
    
    # Paste base images into the grid with jitter and offsets
    for i in range(grid_size):
        for j in range(grid_size):
            code = grid_codes[i][j]
            base_img = base_imgs[code]
            # Calculate the position with jitter
            x = j * cell_size + random.randint(-jitter_amount, jitter_amount)
            y = i * cell_size + random.randint(-jitter_amount, jitter_amount)
            # Ensure the image stays within the boundaries
            x = max(0, min(x, stimulus_size - cell_size))
            y = max(0, min(y, stimulus_size - cell_size))
            stimulus_image.paste(base_img, (x, y), base_img)
    
    # Save the stimulus image
    stimulus_image.save(output_path)

# Example usage
grid_codes = [
    [0, 1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1, 0]
]

output_path = 'stimulus_image_with_jitter.png'
create_stimulus_image(grid_codes, output_path)
print(f'Stimulus image saved as {output_path}')
