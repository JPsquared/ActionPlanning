# MAIN PROJECT EXECUTABLE
import json
import dot_parser
import a_star_github


if __name__ == "__main__":
    print("Action Planning Project")
    # use map of world to get bot position

    # get graph of world from dotfile

    # get balloon starting positions
    with open("test_warehouse_start.json") as json_file:
        start_pos_dict = json.load(json_file)
        print start_pos_dict

    # get balloon ending positions
    with open("test_warehouse_end.json") as json_file:
        end_pos_dict = json.load(json_file)
        print end_pos_dict

    # generate state graph
    # edges need to have the f cost (g cost + h cost) and the decision that resulted in their creation
    # when calling generate children on a state, child states must be possible, i.e. don't create a state where all
    # three balloons are being held at once

    # run A* on state graph to get optimal decision path
    # store decision path in a list

    # execute list of decisions
    # for each edge in decision path
        # if decision is drive
            # get current pos and goal pos
            # run dijkstra's on hopper map to find path of points
            # drive from point to point until goal is reached
        # if decision is pickup balloon
            # run color project to find balloon
            # add balloon to payload
        # if decision is putdown balloon
            # print that the balloon was put down
            # remove balloon from payload
