from sys import argv
from sys import exit
from json import load

def usage():
    print("Usage: ")
    print("python3 parse.py <input file> <output file>")
    exit(-1)

if len(argv) < 3:
    usage()

_ = load(open(argv[1]))

with open(argv[2], "w") as fd:
    for packet in _:
        p = packet["_source"]["layers"]["tcp"]
        src = p['tcp.srcport']
        dst = p['tcp.dstport']
        l   = p['tcp.len']
        seq = p['tcp.seq']
        ack = p['tcp.ack']
        fd.write(f"{src} {dst} {l} {seq} {ack}\n")
