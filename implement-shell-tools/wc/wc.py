import argparse

parser = argparse.ArgumentParser(
    prog="wc", description="Count lines, words, and characters in one or more files."
)

parser.add_argument("-c", action="store_true", help="Count the number of characters.")
parser.add_argument("-w", action="store_true", help="Count the number of words.")
parser.add_argument("-l", action="store_true", help="Count the number of lines.")
parser.add_argument("paths", nargs="+", help="Path(s) to the file(s) to process.")


total_results = {}


args = parser.parse_args()
paths = args.paths
no_flags = not args.c and not args.w and not args.l

for path in paths:
    with open(path, "r") as f:
        content = f.read()

    count_lines = len(content.splitlines())
    count_words = len(content.split())
    count_characters = len(content)

    results = {}

    if no_flags or args.l:
        results["count_lines"] = count_lines

    if no_flags or args.w:
        results["count_words"] = count_words

    if no_flags or args.c:
        results["count_characters"] = count_characters

    for key, value in results.items():
        total_results[key] = total_results.get(key, 0) + value

    print(" ".join(map(str, results.values())), path)

if len(paths) > 1:
    print(" ".join(map(str, total_results.values())), "total")
