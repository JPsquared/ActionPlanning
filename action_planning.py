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


def distance(p1, p2):  # point: (x, y)
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


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
        redDif = current_node.red_location - goal_node.red_location
        purpleDif = current_node.purple_location - goal_node.purple_location
        blueDif = current_node.blue_location - goal_node.blue_location
        greenDif = current_node.green_location - goal_node.green_location
        sumDif = redDif + purpleDif + blueDif + greenDif
        return sumDif/2

    # returns a list of all children that can be generated from this node
    def neighbors(self, node, goal):
        to_return = []
        # create state representations of each action
        # drive to one of the four balloons or one of the four balloon goal locations

        # figure out which balloons are on the bot
        # if any of the four balloons are close, try to pick it up

        # try to drop a balloon off if possible

        # if action == drive (l1, l2)
            # current state must have robot location at l1
            # child state adds robot location l2
            # child state removes robot location l1
            # add child to list

        # if action == pickup(b)
            # current state must have robot carrying at most one balloon, and robot is at same location as desired balloon to pick up
            # child state adds robot carrying new balloon
            # child state removes balloon from location
            # add child to list

        # if action == putdown(b)
            # current state must have robot carrying at least one balloon, and robot is located at position l
            # child state adds ball location is now l, and robot is carrying one less balloon
            # child state removes robot carrying one or both balloons
            # add child to list


    # returns the true distance between two nodes, a and b
    # used to calculate g cost
    def distance_between(self, node_a, node_b):
        # this should probably just be a driving distance value
        # might need to use dijkstra's on the hopper map to calculate this
        locA = node_a.robot_location
        locB = node_b.robot_location
        return distance(locA, locB)

    # returns true if the values for the locations of all the balloons are within a tolerable radius
    def is_goal_reached(self, current_node, goal_node):
        checklist = 0
        if abs(current_node.red_location - goal_node.red_location) < 0.5:
            checklist += 1
        if abs(current_node.purple_location - goal_node.purple_location) < 0.5:
            checklist += 1
        if abs(current_node.blue_location - goal_node.blue_location) < 0.5:
            checklist += 1
        if abs(current_node.green_location - goal_node.green_location) < 0.5:
            checklist += 1
        if checklist == 4:
            return True
        else:
            return False


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
    start_node = None

    # get balloon ending positions
    with open(GOAL_JSON) as json_file:
        end_pos_dict = json.load(json_file)
        print end_pos_dict

    # create goal node using starting balloon positions
    goal_node = None

    # GENERATE STATE GRAPH
    # edges need to have the f cost (g cost + h cost) and the decision that resulted in their creation
    # when calling generate children on a state, child states must be possible, i.e. don't create a state where all
    # three balloons are being held at once
    # THIS MIGHT NOT NEED DONE IF THE A* ALGORITHM DOES IT FOR US

    # RUN A* ON STATE GRAPH TO GET OPTIMAL DECISION PATH
    # store decision path in a list
    a_star_obj = AStar()

    output = a_star_obj.astar(start_node, goal_node)


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
