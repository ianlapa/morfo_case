import numpy as np
from etl.generate_batches import add_white_black_squares

def test_squares_do_not_overlap():
    img = np.zeros((256, 512, 3), dtype=np.uint8)
    modified = add_white_black_squares(img.copy())

    white_mask = np.all(modified == 255, axis=-1)
    black_mask = np.all(modified == 0, axis=-1)

    overlap = np.logical_and(white_mask, black_mask)
    assert not np.any(overlap), "White and black squares should not overlap"
