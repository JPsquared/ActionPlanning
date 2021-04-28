# Parse given dot file to extract useful information from it
from math import sqrt


def distance(p1, p2):  # point: (x, y)
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


def pull_coordinates(s):
    pass


def parse_dotfile(filename):
    dotfile = open(filename, 'r')
    raw = dotfile.read()

    raw_lines = raw.split('\n')
    print raw_lines


parse_dotfile("hopper_graph.dot")
