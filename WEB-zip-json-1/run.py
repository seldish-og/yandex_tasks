import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--sort", default=False, type=bool, action="store_true")
parser.add_argument("data", nargs="*", )
args = parser.parse_args()
print(args.data)


mdic = {}
sorting = False
for i in args.data:
    termp = i.split("=")
    mdic[termp[0]] = termp[1]

keys = list(mdic.keys())
if args.sort:
    keys.sort()

for el in keys:
    print(f"Key: {el} Value: {mdic[el]}")
