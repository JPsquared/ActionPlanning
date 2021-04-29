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
    # generate state graph
    # edges need to have the f cost and the decision that resulted in their creation

    # run A* on state graph to get optimal decision path

    # execute list of decisions

