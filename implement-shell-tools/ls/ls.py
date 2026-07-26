import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="ls",
    description="ls implementation",
)

parser.add_argument("path", nargs="?", help="The file to process", default=".")
parser.add_argument(
    "-1", "--one_per_line", action="store_true", help="one file per line"
)
parser.add_argument("-a", action="store_true", help="Show hidden files")


args = parser.parse_args()

path = Path(args.path)

items = []
for item in sorted(path.iterdir()):
    if args.a or not item.name.startswith("."):
        items.append(item.name)

if args.one_per_line:
    for name in items:
        print(name)
else:
    print(" ".join(items))
