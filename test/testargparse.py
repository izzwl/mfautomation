import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mf', help='mf instance')
parser.add_argument('--wip', help='wip select')
args = parser.parse_args()

print(args.getmf)
print(args.wip)