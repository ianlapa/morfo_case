import numpy as np
import os
import pytest
from etl.analyze_batches import analyze_batch

def test_corrupted_file(tmp_path):
    batch_dir = tmp_path / "batch_test"
    batch_dir.mkdir()

    # Imagem válida
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    np.save(batch_dir / "img_valid.npy", img)

    # Imagem corrompida (arquivo vazio)
    with open(batch_dir / "img_broken.npy", "wb") as f:
        f.write(b"")

    with pytest.raises(Exception):
        analyze_batch(str(batch_dir))
