# MAIN PROJECT EXECUTABLE
import json
import dot_parser
from a_star_github import AStar, find_path
import dijkstras_algorithm
from turtleAPI import robot
from math import sqrt

USING_BOT = True
DOTFILE = "hopper_graph.dot"
START_JSON = "states/start.json"
GOAL_JSON = "states/simple.json"


# defines the structure of the data contained in each node in the A* graph
class StateNode(AStar):
    def __init__(self, red, purple, blue, green, robot, decision):
        # each of the parameters is a location stored in tuple form
        # if None, then the balloon is being held
        self.red_location = red
        self.purple_location = purple
        self.blue_location = blue
        self.green_location = green
        self.robot_location = robot
        # stores the decision that was made in the previous node that caused this node to be created
        # facilitates recreation of decision path once path is found
        self.decision = decision

    def heuristic_cost_estimate(self, current_node, goal_node):
        # a good starter heuristic is to take the difference in position of each of the balloons and to
        # sum them and then divide by 2
        pass

    # returns a list of all children that can be generated from this node
    def neighbors(self, node):
        to_return = []
        # create state representations of each action
        # drive to one of the four balloons or one of the four balloon goal locations

        # if any of the four balloons are close, try to pick it up
        node

        # try to drop a balloon off if possible

    # returns the true distance between two nodes, a and b
    # used to calculate g cost
    def distance_between(self, node_a, node_b):
        # this should probably just be a driving distance value
        # might need to use dijkstra's on the hopper map to calculate this
        pass

    # returns true if the values for the locations of all the balloons are in the right place
    def is_goal_reached(self, current_node, goal_node):
        pass

# def distance(p1, p2):  # point: (x, y)
#     return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


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
    with open(START_JSON) as json_file:
        start_pos_dict = json.load(json_file)
        print start_pos_dict

    # create start node using starting balloon positions

    # get balloon ending positions
    with open(GOAL_JSON) as json_file:
        end_pos_dict = json.load(json_file)
        print end_pos_dict

    # create goal node using starting balloon positions

    # GENERATE STATE GRAPH
    # edges need to have the f cost (g cost + h cost) and the decision that resulted in their creation
    # when calling generate children on a state, child states must be possible, i.e. don't create a state where all
    # three balloons are being held at once
    # THIS MIGHT NOT NEED DONE IF THE A* ALGORITHM DOES IT FOR US

    # RUN A* ON STATE GRAPH TO GET OPTIMAL DECISION PATH
    # store decision path in a list
    output = find_path(start_node, goal_node,
                       neighbors_fnct=neighbors,
                       reversePath=False,
                       heuristic_cost_estimate_fnct=heuristic,
                       distance_between_fnct=distance,
                       is_goal_reached_fnct=is_goal_reached)

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
