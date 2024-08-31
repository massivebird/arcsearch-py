import re, os, yaml

archive_root = "/home/penguino/game-archive"

def clean_filename(s: str) -> str:
    s = re.sub(r'\(.*\)|\[.*\]', "", s)
    extension_idx = re.search(r'\.', s)

    if extension_idx != None:
        s = s[0:extension_idx.end() - 1]

    return s

config_file = open(archive_root + "/config.yaml", 'r')
config_yaml = yaml.safe_load(config_file)

system_labels = list(config_yaml["systems"])

for root, subDirectory, files in os.walk(archive_root):

    dividers = re.search(r'/', root)

    if dividers == None:
        continue # no idea how this could happen

    skip_it = True
    for label in system_labels:
        if root.__contains__(str(label)):
            skip_it = False
            break

    if skip_it:
        continue

    for name in files:
        print(clean_filename(name))
