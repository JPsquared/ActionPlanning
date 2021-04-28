# MAIN PROJECT EXECUTABLE
import json
from dijkstras_algorithm import Graph


if __name__ == "__main__":
    print("Action Planning Project")
    # use map of world to get bot position

    # get graph of world from dotfile

    # create graph
    g = Graph(10)  # call with number of nodes in graph
    # call add_edge()
    # do in a loop

    # call dijkstra's
    g.dijkstra(0)  # call with start node
    # call show_path(x, y)
    g.show_path(0, 9)  # call with start and end node labels
