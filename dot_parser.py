# Parse given dot file to extract useful information from it
from re import search


def parse_dotfile(filename):
    dotfile = open(filename, 'r')
    raw = dotfile.read()
    # split text into lines by newline char
    raw_lines = raw.split('\n')
    # get rid of the first line
    raw_lines.pop(0)
    # create dict of node keys and node locations
    node_list = {}
    graph = {}
    for i in range(len(raw_lines)):
        # strip away leading whitespace
        string = raw_lines[i].strip()
        # pull key value from beginning of string
        parts = string.split(' ', 1)
        if parts[0] == '}':
            break
        elif parts[1][0] == '[':  # these are lines that contain node locations
            key = parts[0]
            x = float(search(r'\(-?\d+\.?\d*,\s', parts[1]).group()[1:-2])
            y = float(search(r',\s-?\d+\.?\d*\)', parts[1]).group()[2:-1])
            location = (x, y)
            node_list[key] = location
        elif parts[1][0] == '-':  # these are lines that contain graph connections
            key = parts[0]
            connection = search(r'[0-9][ab]', parts[1]).group()
            print connection
            if key in graph:
                graph[key].append(connection)
            else:
                graph[key] = [connection]

    return node_list, graph


if __name__ == "__main__":
    parse_dotfile("hopper_graph.dot")
