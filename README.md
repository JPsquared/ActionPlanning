# ActionPlanning

## [JSON parsing instructions](https://cpython-test-docs.readthedocs.io/en/latest/library/json.html)

## Description

Warehouse Organization Project
More and more, robots are responsible for organizing items in warehouses. We are going 
to use our robots to autonomously maintain an organized balloon warehouse.

Balloons will be scattered throughout the half of the first floor of Hopper we have a 
map for. You will have a record of about where each is. The foreman wants all the 
balloons reorganized! You expect management will do this a lot, so you’ve decided to 
program your robot to do it autonomously, where you merely have to give the robot a 
record of the current state of the warehouse, and a second for the desired state of 
the warehouse, and it drives around moving balloons. (Of course, our Turtlebots can’t 
“pick up” anything, so we’ll just have it print out “PICK UP (color) BALLOON” and 
“PUT DOWN (color) BALLOON” in place of those actions for an onboard arm we don’t have. 
This is how Shakey “performed” much of its behavior, as well, so we’re in good company.)

Your robot can carry a maximum of two balloons at once. It should perform its task in 
as short a time as possible.

Warehouse states will be stored as .json files, the text of which 
might look like this:

```
{
  "RED": [
    3,
    5
  ],
  "BLUE": [
    7.3,
    9.1
  ],
  "YELLOW": [
    -32.1,
    -5.9
  ]
}
```

In this one the red balloon, for example, is located at ```(x, y) = (3, 5)``` in the map frame. 
If read as a .json, it will load conveniently as a dictionary without you having to 
write a parser.

Define a logic
Define a logic which allows you to fully describe the world state. Each action should 
have the preconditions, addition, and deletions of the state that allow you to predict 
the world state after taking each of the actions. Write these out, you’ll turn them in.

You might, for example, define three actions, DRIVE, PICKUP, and PUTDOWN. DRIVE drives 
the robot to a location without hitting a wall (that is, it’s the navigation project). 
PICKUP picks up a specified object and puts it in the robot’s payload (the robot and 
the object would need to be in about the same place). PUTDOWN removes an object from 
the robot’s payload and puts it at the robot’s current location.

Perform graph search
Print out a sequence of actions that will result in the old warehouse state being 
converted to the new warehouse state in a minimal amount of time.

Perform the actions
Drive around, correctly approaching the needed balloons, and printing the pickups and 
putdown commands at the right time.