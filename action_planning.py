# MAIN PROJECT EXECUTABLE
import json
import dot_parser
from a_star_github import AStar, find_path
import dijkstras_algorithm
# from turtleAPI import robot
from math import sqrt

USING_BOT = True
DOTFILE = "hopper_graph.dot"
START_JSON = "states/start.json"
GOAL_JSON = "states/simple.json"
PICKUP_RADIUS = 2  # radius within which the option to pick up a balloon is available


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
        redDif = distance(current_node.red_location, goal_node.red_location)
        purpleDif = distance(current_node.purple_location, goal_node.purple_location)
        blueDif = distance(current_node.blue_location, goal_node.blue_location)
        greenDif = distance(current_node.green_location, goal_node.green_location)
        sumDif = redDif + purpleDif + blueDif + greenDif
        return sumDif/2

    # returns a list of all children that can be generated from this node
    def neighbors(self, node, goal):
        to_return = []

        # create state representations of each action
        # drive to one of the four balloons or one of the four balloon goal locations

        # figure out which balloons are on the bot
        onBot = {'red': False, 'purple': False, 'blue': False, 'green': False}
        if self.red_location is not None:
            onBot['red'] = True
        if self.purple_location is not None:
            onBot['purple'] = True
        if self.blue_location is not None:
            onBot['blue'] = True
        if self.green_location is not None:
            onBot['green'] = True

        # figure out how many balloons are on the bot
        numOnBot = 0
        for key in onBot.keys():
            if onBot[key]:
                numOnBot += 1

        if numOnBot > 2:
            print 'ERROR: MORE THAN TWO BALLOONS ON BOT IN STATE'

        # if any of the four balloons are close, try to pick it up

        # try to drop a balloon off if possible

        # if action == drive (l1, l2)
            # current state must have robot location at l1
            # child state adds robot location l2
            # child state removes robot location l1
            # add child to list
        to_return.append(StateNode(self.red_location, self.purple_location, self.blue_location, self.green_location, goal.red_location, 'DRIVE GOAL RED'))
        to_return.append(StateNode(self.red_location, self.purple_location, self.blue_location, self.green_location, goal.purple_location, 'DRIVE GOAL PURPLE'))
        to_return.append(StateNode(self.red_location, self.purple_location, self.blue_location, self.green_location, goal.blue_location, 'DRIVE GOAL BLUE'))
        to_return.append(StateNode(self.red_location, self.purple_location, self.blue_location, self.green_location, goal.green_location, 'DRIVE GOAL GREEN'))

        # of the balloons not on the bot, create nodes to drive to them also
        for key in onBot.keys():
            if not onBot[key]:
                if key == 'red':
                    to_return.append(StateNode(self.red_location, self.purple_location, self.blue_location, self.green_location, self.red_location, 'DRIVE CURRENT RED'))
                if key == 'purple':
                    to_return.append(StateNode(self.red_location, self.purple_location, self.blue_location, self.green_location, self.purple_location, 'DRIVE CURRENT PURPLE'))
                if key == 'blue':
                    to_return.append(StateNode(self.red_location, self.purple_location, self.blue_location, self.green_location, self.blue_location, 'DRIVE CURRENT BLUE'))
                if key == 'green':
                    to_return.append(StateNode(self.red_location, self.purple_location, self.blue_location, self.green_location, self.green_location, 'DRIVE CURRENT GREEN'))

        # if action == pickup(b)
            # current state must have robot carrying at most one balloon, and robot is at same location as desired balloon to pick up
            # child state adds robot carrying new balloon
            # child state removes balloon from location
            # add child to list
        for key in onBot.keys():
            if numOnBot < 2:  # if there are less than two balloons on board the bot
                if not onBot[key]:  # if the balloon in question is not on the bot
                    if key == 'red':
                        if distance(self.red_location, self.robot_location) <= PICKUP_RADIUS:
                            to_return.append(StateNode(None, self.purple_location, self.blue_location, self.green_location, self.robot_location, 'PICKUP RED'))
                    if key == 'purple':
                        if distance(self.purple_location, self.robot_location) <= PICKUP_RADIUS:
                            to_return.append(StateNode(self.red_location, None, self.blue_location, self.green_location, self.robot_location, 'PICKUP PURPLE'))
                    if key == 'blue':
                        if distance(self.blue_location, self.robot_location) <= PICKUP_RADIUS:
                            to_return.append(StateNode(self.red_location, self.purple_location, None, self.green_location, self.robot_location, 'PICKUP BLUE'))
                    if key == 'green':
                        if distance(self.green_location, self.robot_location) <= PICKUP_RADIUS:
                            to_return.append(StateNode(self.red_location, self.purple_location, self.blue_location, None, self.robot_location, 'PICKUP GREEN'))

        # if action == putdown(b)
            # current state must have robot carrying at least one balloon, and robot is located at position l
            # child state adds ball location is now l, and robot is carrying one less balloon
            # child state removes robot carrying one or both balloons
            # add child to list
        # ADD CHILDREN STATES AFTER PUTDOWN CALL
        for key in onBot.keys():
            if onBot[key]:
                # this balloon is on the bot and can be put down at the current location
                # create a new state and add it to the list
                # IF THIS RESULTS IN UNEXPECTED BEHAVIOR, TRY CHANGING SELF TO NODE
                if key == 'red':
                    to_return.append(StateNode(self.robot_location, self.purple_location, self.blue_location, self.green_location, self.robot_location, 'PUTDOWN RED'))
                if key == 'purple':
                    to_return.append(StateNode(self.red_location, self.robot_location, self.blue_location, self.green_location, self.robot_location, 'PUTDOWN PURPLE'))
                if key == 'blue':
                    to_return.append(StateNode(self.red_location, self.purple_location, self.robot_location, self.green_location, self.robot_location, 'PUTDOWN BLUE'))
                if key == 'green':
                    to_return.append(StateNode(self.green_location, self.purple_location, self.blue_location, self.robot_location, self.robot_location, 'PUTDOWN GREEN'))

        return [to_return]

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
        if distance(current_node.red_location, goal_node.red_location) < 0.5:
            checklist += 1
        if distance(current_node.purple_location, goal_node.purple_location) < 0.5:
            checklist += 1
        if distance(current_node.blue_location, goal_node.blue_location) < 0.5:
            checklist += 1
        if distance(current_node.green_location, goal_node.green_location) < 0.5:
            checklist += 1
        if checklist == 4:
            return True
        else:
            return False

    def __str__(self):
        return str({'red': self.red_location,
                    'purple': self.purple_location,
                    'blue': self.blue_location,
                    'green': self.green_location,
                    'pos': self.robot_location,
                    'decision': self.decision
                    })


if __name__ == "__main__":
    print("Action Planning Project")
    # create robot
    # rbt = robot()

    # use map of world to get bot position
    # current_position = rbt.getMCLPose()
    current_position = None

    # get graph of world from dotfile
    node_list, graph = dot_parser.parse_dotfile(DOTFILE)

    # get balloon starting positions
    start_pos_dict = json.load(open(START_JSON))

    # create start node using starting balloon positions
    start_red_tuple = (start_pos_dict['RED'][0], start_pos_dict['RED'][1])
    start_purple_tuple = (start_pos_dict['PURPLE'][0], start_pos_dict['PURPLE'][1])
    start_blue_tuple = (start_pos_dict['BLUE'][0], start_pos_dict['BLUE'][1])
    start_green_tuple = (start_pos_dict['GREEN'][0], start_pos_dict['GREEN'][1])

    start_node = StateNode(start_red_tuple, start_purple_tuple, start_blue_tuple, start_green_tuple, current_position, None)

    # get balloon ending positions
    goal_pos_dict = json.load(open(GOAL_JSON))

    # create goal node using starting balloon positions
    goal_red_tuple = (goal_pos_dict['RED'][0], goal_pos_dict['RED'][1])
    goal_purple_tuple = (goal_pos_dict['PURPLE'][0], goal_pos_dict['PURPLE'][1])
    goal_blue_tuple = (goal_pos_dict['BLUE'][0], goal_pos_dict['BLUE'][1])
    goal_green_tuple = (goal_pos_dict['GREEN'][0], goal_pos_dict['GREEN'][1])

    goal_node = StateNode(goal_red_tuple, goal_purple_tuple, goal_blue_tuple, goal_green_tuple, None, None)

    # TEST SECTION #
    print start_node
    print goal_node
    # END TEST SECTION #

    # GENERATE STATE GRAPH
    # edges need to have the f cost (g cost + h cost) and the decision that resulted in their creation
    # when calling generate children on a state, child states must be possible, i.e. don't create a state where all
    # three balloons are being held at once
    # THIS MIGHT NOT NEED DONE IF THE A* ALGORITHM DOES IT FOR US

    # RUN A* ON STATE GRAPH TO GET OPTIMAL DECISION PATH
    # store decision path in a list
    path = find_path(start_node, goal_node,
                     StateNode.neighbors,
                     False,
                     StateNode.heuristic_cost_estimate,
                     StateNode.distance_between,
                     StateNode.is_goal_reached)

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
    for node in path:
        decision = node.data.decision
