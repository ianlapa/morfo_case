import numpy as np
import os

def stats(arr):
    arr = np.array(arr)
    return {
        "avg": arr.mean(),
        "std": arr.std(),
        "min": arr.min(),
        "max": arr.max()
    }

def analyze_batch(batch_path):
    white_counts = []
    black_counts = []

    for file in os.listdir(batch_path):
        if file.endswith(".npy"):
            img = np.load(os.path.join(batch_path, file))
            white = np.all(img == 255, axis=-1)
            black = np.all(img == 0, axis=-1)
            white_counts.append(np.sum(white))
            black_counts.append(np.sum(black))

    return {
        "white": stats(white_counts),
        "black": stats(black_counts),
    }

if __name__ == "__main__":
    for i in range(1, 6):
        path = f"data/batch_{i}"
        results = analyze_batch(path)
        print(f"Batch {i}:")
        print("  White:", results["white"])
        print("  Black:", results["black"])