# Parse given dot file to extract useful information from it
from math import sqrt
import re


def distance(p1, p2):  # point: (x, y)
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


def pull_coordinates(s):
    pass


def parse_dotfile(filename):
    dotfile = open(filename, 'r')
    raw = dotfile.read()
    # split text into lines by newline char
    raw_lines = raw.split('\n')
    # get rid of the first line
    raw_lines.pop(0)
    # create list of node keys and node locations
    node_list = []
    for line in raw_lines:
        # strip away leading whitespace
        string = line.strip()
        # pull key value from beginning of string
        parts = string.split(' ', 1)
        if parts[1][0] != '[':
            break
        key = parts[0]
        print parts[0]  # here we see all unique key values
        print parts[1]  # here is the rest of the string that contains the location
        flag = re.match(r'\(-?\d+\.?\d*,\s-?\d+\.?\d*\)', parts[1])
        print flag
        location = None
        if flag:
            print flag.group()
            location = tuple(flag.group())
        else:
            print "No match"
        node_list.append((key, location))


if __name__ == "__main__":
    parse_dotfile("hopper_graph.dot")
