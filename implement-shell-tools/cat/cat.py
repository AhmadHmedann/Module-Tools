import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="implement cat",
)

parser.add_argument("paths", nargs="+", help="The file to process")
parser.add_argument("-n", action="store_true", help="Number all lines")
parser.add_argument("-b", action="store_true", help="Number non-empty lines only")

args = parser.parse_args()
counter = 1

for path in args.paths:
    with open(path, "r") as f:
        for line in f:
            if args.n:
                print(f"\t{counter} {line}", end="")
                counter += 1
            elif args.b:
                if line.strip() != "":
                    print(f"\t{counter} {line}", end="")
                    counter += 1
                else:
                    print(f"\t {line}", end="")
            else:
                print(f" {line}", end="")
