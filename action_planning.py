# MAIN PROJECT EXECUTABLE
import json
import dot_parser
import a_star_github
import dijkstras_algorithm
from turtleAPI import robot
from math import sqrt

USING_BOT = True
DOTFILE = "hopper_graph.dot"


# defines the structure of the data contained in each node in the A* graph
class StateNode:
    def __init__(self, red, purple, blue, green, robot):  # each of the parameters is a location stored in tuple form
        # if None, then the balloon is being held
        self.red_location = red
        self.purple_location = purple
        self.blue_location = blue
        self.green_location = green
        self.robot_location = robot


def heuristic(current_node, goal_node):
    # a good starter heuristic is to take the difference in position of each of the balloons and to
    # sum them and then divide by 2
    pass


# returns a list of all children that can be generated from this node
def neighbors(current_node):
    pass


# returns the true distance between two nodes, a and b
# used to calculate g cost
def distance(node_a, node_b):
    pass


def distance(p1, p2):  # point: (x, y)
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


if __name__ == "__main__":
    print("Action Planning Project")
    # create robot
    if USING_BOT:
        rbt = robot()

    # use map of world to get bot position
    if USING_BOT:
        current_position = rbt.getMCLPose()

    # get graph of world from dotfile
    node_list, graph = dot_parser.parse_dotfile(DOTFILE)

    # get balloon starting positions
    with open("test_warehouse_start.json") as json_file:
        start_pos_dict = json.load(json_file)
        print start_pos_dict

    # get balloon ending positions
    with open("test_warehouse_end.json") as json_file:
        end_pos_dict = json.load(json_file)
        print end_pos_dict

    # GENERATE STATE GRAPH
    # edges need to have the f cost (g cost + h cost) and the decision that resulted in their creation
    # when calling generate children on a state, child states must be possible, i.e. don't create a state where all
    # three balloons are being held at once

    # RUN A* ON STATE GRAPH TO GET OPTIMAL DECISION PATH
    # store decision path in a list

    # EXECUTE LIST OF DECISIONS
    # for each edge in decision path
        # if decision is drive
            # get current pos and goal pos
            # run dijkstra's on hopper map to find path of points
            # drive from point to point using PID controller until goal is reached
        # if decision is pickup balloon
            # run color project to find balloon
            # add balloon to payload
        # if decision is putdown balloon
            # print that the balloon was put down
            # remove balloon from payload
