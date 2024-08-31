import re, os

archive_root = "/home/penguino/game-archive"

def clean_filename(s: str) -> str:
    s = re.sub(r'\(.*\)|\[.*\]', "", s)
    extension_idx = re.search(r'\.', s)

    if extension_idx != None:
        s = s[0:extension_idx.end() - 1]

    return s

for _, _, files in os.walk(archive_root):
    for name in files:
        print(clean_filename(name))
