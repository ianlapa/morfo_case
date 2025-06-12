import numpy as np
import os

def overlap(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return not (ax2 <= bx1 or ax1 >= bx2 or ay2 <= by1 or ay1 >= by2)

def get_random_square(image_shape, square_size, exclude=[]):
    h, w = image_shape[:2]
    while True:
        x = np.random.randint(0, w - square_size)
        y = np.random.randint(0, h - square_size)
        rect = (x, y, x + square_size, y + square_size)
        if not any(overlap(rect, e) for e in exclude):
            return rect

def add_white_black_squares(img):
    square_size = 50
    white_sq = get_random_square(img.shape, square_size)
    black_sq = get_random_square(img.shape, square_size, exclude=[white_sq])
    img[white_sq[1]:white_sq[3], white_sq[0]:white_sq[2]] = 255
    img[black_sq[1]:black_sq[3], black_sq[0]:black_sq[2]] = 0
    return img

def random_crop(img, crop_size=200):
    h, w = img.shape[:2]
    x = np.random.randint(0, w - crop_size)
    y = np.random.randint(0, h - crop_size)
    return img[y:y+crop_size, x:x+crop_size]

def generate_batch(batch_id, output_dir="data"):
    os.makedirs(f"{output_dir}/batch_{batch_id}", exist_ok=True)
    for i in range(20):
        img = np.random.randint(0, 256, (256, 512, 3), dtype=np.uint8)
        img = add_white_black_squares(img)
        img = random_crop(img)
        np.save(f"{output_dir}/batch_{batch_id}/img_{i}.npy", img)

if __name__ == "__main__":
    for i in range(1, 6):
        generate_batch(i)