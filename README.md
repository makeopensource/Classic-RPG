# Classic RPG

### Prerequisites

* Python >= 3.8


### Installation

`python3 -m pip install -r requirements.txt`

`python3 game-2.py`


# Configuration

The crpg API is now configured via a filetype called a 
".dl" file (dungeon layout). DLs have a very specific format
that allow them to be parsed. 

The first part is a list of nodes for the decision graph. Each 
node has a unique tag, its name, description, and
any other parameters that need to be passed to the constructor 
to create the appropriate object.

*Three dashes separate the first and second parts.*

The second part is a list of connections between nodes. Instead of
passing some sort of unique identifier for each node, you use the 
tag from the first part to identify the node. Then, you can use one 
of two symbols to denote a connection between two nodes:

- `node_a -> node_b` means node_a points towards node_b (in only one direction)
- `node_a <-> node_b` means node_a points to node_b, and vice versa

If we want to expand the API for connections, we can always add more symbols
for parsing. One I was thinking about is `\->`, which would denote an
"ending" connection (to signal destroying the path to reach the current action)

# Potion

1) Know the attributes of your potion

2) Go to **builtin.py** -> **Potion** and find **Potion** class. This is where you initialize the potion. **NOTE:** You don't assume the player is going to use an object. This is merely initialization. Tip: Initialize the logic of your object here. 

3) Do not forget to go to **crpg.py** -> **generate()** iff you are:
    - creating a new potion type. 
        - go to the first for loop and look for the first if statement. 
        - remember to include your new object type in n_types

Potion encoding:
> nodeID | potion | po(-type of potion -operation) | Description
> Example: 3 | potion | po-health-collect-[options] | Pick up potion

Health:
nodeID | potion | po(-health-collect-[amount]) | Description
