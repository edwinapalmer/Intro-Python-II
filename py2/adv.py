from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room["foyer"].items.append(Item(1, "Gems", "A bag of beautiful gems"))
room["overlook"].items.append(Item(2, "Fossils", "A bag of old fossils"))
room["narrow"].items.append(Item(3, "Candies", "A bag of assorted candies"))
room["treasure"].items.append(Item(4, "Cake", "Delicious butter pound cake"))
room["outside"].items.append(Item(5, "Gnome", "An old Gnome from Norway"))



# Make a new player object that is currently in the 'outside' room.
name = input("Enter your name: ")
player = Player(name, room['outside'], [])


# input = ['n', 's', 'e', 'w']
# selection = ['y']
move = ''

    
    # current = rooms[player.current_room]
    # * Prints the current room name
    # print(player.current_room)
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    # player.print_items()

while True:
    print(
         f"Current Room: {player.current_room.name}\n Current Items {player.items}\n Items in the Room {player.current_room.items}\n {player.current_room.description}")
    command = input(
         "Enter n: Move north\nEnter s: Move south\nEnter e: Move east\nEnter w: Move west\nEnter q: Enter q to quit\n")
    print(f"You moved {command}")
    
    # print(command)

    if command == 'q':
        break
    elif command[0] == 'n':
        # check if the player can move to the north
        # if there is, set that north room as the player's location
        player.current_room = player.current_room.n_to
   
    elif command[0] == 's':
        player.current_room = player.current_room.s_to
    elif command[0] == 'e':
        player.current_room = player.current_room.e_to
    elif command[0] == 'w':
        player.current_room = player.current_room.w_to
    else:
        print('Incorrect input, try again!')