"""List every file in a folder with size and SHA-256, to paste into the Zenodo description / data README.
   python make_manifest.py /path/to/data_folder > MANIFEST.csv"""
import hashlib, os, sys
root = sys.argv[1]
print("file,size_MB,sha256")
for d, _, fs in os.walk(root):
    for f in sorted(fs):
        p = os.path.join(d, f); h = hashlib.sha256()
        with open(p, "rb") as fh:
            for b in iter(lambda: fh.read(1 << 20), b""): h.update(b)
        print(f"{os.path.relpath(p, root)},{os.path.getsize(p)/1e6:.2f},{h.hexdigest()}")
