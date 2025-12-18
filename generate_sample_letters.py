"""
Utility to recreate the tiny 28x28 grayscale PNG samples used for external handwritten-letter inference.

Binary assets are intentionally excluded from version control; run this script to regenerate the six sample files:
- my_letter.png
- a.png
- b.png
- ma.png
- k.png
- wpng.png
"""
from __future__ import annotations

import base64
from pathlib import Path

# Base64-encoded PNG payloads (28x28 grayscale) captured from the prior samples.
SAMPLES = {
    "my_letter.png": "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAAAAABXZoBIAAAAJElEQVR4nGP4DwQMQPAfCcD4DMNQEh0QLznovDKoJHGBYSQJAEw2Vce6EkkWAAAAAElFTkSuQmCC",
    "a.png": "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAAAAABXZoBIAAAALElEQVR4nGP4DwUMSAAuRoQkihCcTVgSWQqZT2tJdEC85EC4duhI4gLDSBIA6zdNz7AljJAAAAAASUVORK5CYII=",
    "b.png": "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAAAAABXZoBIAAAAJUlEQVR4nGP4DwQMaOA/FDAQJfkfDhC8wSs5UvxJ7xDCBYaRJABCjz3feZ9qEwAAAABJRU5ErkJggg==",
    "ma.png": "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAAAAABXZoBIAAAAM0lEQVR4nGP4DwQMQPAfCcD4DERJIqQRPGIlGTDZREkiC5MqiYUmWpK8EBoJkrjAMJIEAJQyPd856NDfAAAAAElFTkSuQmCC",
    "k.png": "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAAAAABXZoBIAAAAPUlEQVR4nGP4DwQMQPAfDhA8BpIkUdgkSKJZQLQkqhSxkhDw/z/pkuTbSZk/MdgkSZIfnyheIyiJCwwjSQCNNWmzHAVr2QAAAABJRU5ErkJggg==",
    "wpng.png": "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAAAAABXZoBIAAAALUlEQVR4nGP4DwQMQPAfCcD4DINaEoMmUpIBCugnifAMgjd4JcmLFVxgGEkCAJQyLe+hRI8gAAAAAElFTkSuQmCC",
}


def write_samples(output_dir: Path | str = ".") -> None:
    """Decode and write all sample images into *output_dir*.

    Args:
        output_dir: Directory where the PNGs should be written.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    for filename, b64 in SAMPLES.items():
        data = base64.b64decode(b64)
        target = out_path / filename
        target.write_bytes(data)
        print(f"Wrote {target} ({len(data)} bytes)")


if __name__ == "__main__":
    write_samples()
