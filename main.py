import re, os, yaml, sys

archive_root = "/home/penguino/game-archive"

args = sys.argv

if len(args) == 1:
    print("Error: please provide a query.")
    sys.exit(1)

query = args[1]

config_file = open(archive_root + "/config.yaml", 'r')
config_yaml = yaml.safe_load(config_file)

def clean_filename(s: str) -> str:
    s = re.sub(r'\(.*\)|\[.*\]', "", s)
    extension_idx = re.search(r'\.', s)

    if extension_idx != None:
        s = s[0:extension_idx.end() - 1]

    return s

class GameSystem:
    def __init__(self, path, name, r, g, b):
        self.path = path
        self.pretty_string = f"\033[38;2;{r};{g};{b}m{name}\033[0m"

    def __str__(self) -> str:
        return self.pretty_string

    def get_path(self) -> str:
        return self.path

# Compile game systems from archive configuration file
systems = []
for label in config_yaml["systems"]:
    sys = config_yaml['systems'][label]
    color = sys['color']
    systems.append(GameSystem(sys['path'], sys['display_name'], color[0], color[1], color[2]))

for root, subDirectory, files in os.walk(archive_root):
    matching_system = None
    for system in systems:
        if f"{archive_root}/{system.path}" in root:
            matching_system = system

    # If this path does not correspond to a defined system,
    # then continue to the next path
    if matching_system == None:
        continue

    for filename in files:
        if re.match(query, filename, re.IGNORECASE):
            print(f"[{matching_system}] " + clean_filename(filename))
