#!/usr/bin/env python3
"""Remove or detect hidden metadata (GPS location, camera details) in JPEG and PNG images.

Usage:
  python3 tools/strip-metadata.py PATH [PATH ...]          strip metadata in place
  python3 tools/strip-metadata.py --check PATH [PATH ...]  report images that still have metadata; exit 1 if any

PATH can be a file or a folder (searched recursively). Only the Python standard library is used.

Orientation: phones often store "rotate this photo" in metadata. Stripping it can make a photo appear sideways, so
rotate photos for real (for example `sips -r 90 photo.jpg`) before or after stripping if one looks wrong.
"""

import sys
from pathlib import Path

JPEG_EXTS = {".jpg", ".jpeg"}
PNG_EXTS = {".png"}
# JPEG segments that carry EXIF/GPS (APP1), Photoshop/IPTC (APP13), and other app data. APP0 (JFIF), APP2 (ICC color
# profile) and APP14 (Adobe color transform) are kept because they affect how colors display.
JPEG_DROP_MARKERS = {0xE1, 0xE3, 0xE4, 0xE5, 0xE6, 0xE7, 0xE8, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEF, 0xFE}
PNG_DROP_CHUNKS = {b"eXIf", b"tEXt", b"zTXt", b"iTXt", b"tIME"}


def jpeg_segments(data):
    """Yield (marker, start, end) for each header segment before the image data begins."""
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG")
    pos = 2
    while pos < len(data):
        if data[pos] != 0xFF:
            raise ValueError(f"bad JPEG segment at byte {pos}")
        marker = data[pos + 1]
        if marker == 0xDA:  # start of scan: the rest is image data
            yield marker, pos, len(data)
            return
        length = int.from_bytes(data[pos + 2 : pos + 4], "big")
        yield marker, pos, pos + 2 + length
        pos += 2 + length


def png_chunks(data):
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    pos = 8
    while pos < len(data):
        length = int.from_bytes(data[pos : pos + 4], "big")
        ctype = data[pos + 4 : pos + 8]
        end = pos + 12 + length
        yield ctype, pos, end
        pos = end


def find_metadata(path, data):
    ext = path.suffix.lower()
    if ext in JPEG_EXTS:
        return [f"JPEG APP{m - 0xE0}" if m != 0xFE else "JPEG comment"
                for m, _, _ in jpeg_segments(data) if m in JPEG_DROP_MARKERS]
    if ext in PNG_EXTS:
        return [c.decode() for c, _, _ in png_chunks(data) if c in PNG_DROP_CHUNKS]
    return []


def strip(path, data):
    ext = path.suffix.lower()
    if ext in JPEG_EXTS:
        out = data[:2] + b"".join(data[s:e] for m, s, e in jpeg_segments(data) if m not in JPEG_DROP_MARKERS)
    elif ext in PNG_EXTS:
        out = data[:8] + b"".join(data[s:e] for c, s, e in png_chunks(data) if c not in PNG_DROP_CHUNKS)
    else:
        return False
    if out != data:
        path.write_bytes(out)
        return True
    return False


def image_files(paths):
    for p in map(Path, paths):
        files = sorted(p.rglob("*")) if p.is_dir() else [p]
        for f in files:
            if f.is_file() and f.suffix.lower() in JPEG_EXTS | PNG_EXTS | {".heic", ".heif", ".tif", ".tiff"}:
                yield f


def main(argv):
    check = "--check" in argv
    paths = [a for a in argv if a != "--check"]
    if not paths:
        print(__doc__)
        return 2
    problems = 0
    for f in image_files(paths):
        ext = f.suffix.lower()
        if ext not in JPEG_EXTS | PNG_EXTS:
            print(f"{f}: {ext} files can carry location data; convert to .jpg first (sips -s format jpeg)")
            problems += 1
            continue
        data = f.read_bytes()
        try:
            found = find_metadata(f, data)
        except ValueError as e:
            print(f"{f}: could not read ({e})")
            problems += 1
            continue
        if check:
            if found:
                print(f"{f}: still has metadata ({', '.join(found)})")
                problems += 1
        elif strip(f, data):
            print(f"{f}: removed {', '.join(found)}")
    if check:
        print("No hidden metadata found." if not problems else
              f"{problems} image(s) need attention. Run: python3 tools/strip-metadata.py site")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
