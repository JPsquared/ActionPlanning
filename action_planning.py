# MAIN PROJECT EXECUTABLE
import json
import dijkstras_algorithm
import dot_parser


if __name__ == "__main__":
    print("Action Planning Project")
    # use map of world to get bot position

    # get graph of world from dotfile

    # get balloon starting positions
    with open("test_warehouse_start.json") as json_file:
        start_pos = json.load(json_file)
        print start_pos
    # get balloon ending positions
    with open("test_warehouse_end.json") as json_file:
        end_pos = json.load(json_file)
        print end_pos
    # create graph
    # g = Graph(10)  # call with number of nodes in graph
    # call add_edge()
    # do in a loop

    # call dijkstra's
    # g.dijkstra(0)  # call with start node
    # call show_path(x, y)
    # g.show_path(0, 9)  # call with start and end node labels
