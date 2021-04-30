# Parse given dot file to extract useful information from it
from math import sqrt
import re
import random, string


def distance(p1, p2):  # point: (x, y)
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


def parse_dotfile(filename):
    dotfile = open(filename, 'r')
    raw = dotfile.read()
    # split text into lines by newline char
    raw_lines = raw.split('\n')
    # get rid of the first line
    raw_lines.pop(0)
    # create dict of node keys and node locations
    node_list = {}
    for i in range(len(raw_lines)):
        # strip away leading whitespace
        string = raw_lines[i].strip()
        # pull key value from beginning of string
        parts = string.split(' ', 1)
        if parts[1][0] != '[':
            break
        key = parts[0]
        x = float(re.search(r'\(-?\d+\.?\d*,\s', parts[1]).group()[1:-2])
        y = float(re.search(r',\s-?\d+\.?\d*\)', parts[1]).group()[2:-1])
        location = (x, y)
        node_list[key] = location
    print node_list.keys()


if __name__ == "__main__":
    parse_dotfile("hopper_graph.dot")
