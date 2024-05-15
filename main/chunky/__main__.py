import argparse

from chunky.src.chunky_join import join
from chunky.src.chunky_split import split

parser = argparse.ArgumentParser()
parser.add_argument("command", choices=["join", "split"])
parser.add_argument("path")
parser.add_argument("-s", "--size", help="['split' only] max size of chunks", default=10, type=int)

args = parser.parse_args()

command = args.command
path = args.path
size = args.size

if command == "split":
    split(path, size)
elif command == "join":
    join(path)
