# Daniel Buck

# The dictionary links a room to other rooms
rooms = {
    'Den': {'North': 'Study', 'East': 'Kitchen', 'South': 'Dining Room', 'West': 'Patio'},
    'Patio': {'East': 'Den', 'item': 'Brick'},
    'Study': {'East': 'Bedroom', 'South': 'Den', 'item': 'Pepper spray'},
    'Bedroom': {'West': 'Study', 'item': 'Robber'},
    'Dining Room': {'North': 'Den', 'East': 'Cellar', 'item': 'Candlestick'},
    'Cellar': {'West': 'Dining Room', 'item': 'Wine bottle'},
    'Kitchen': {'North': 'Pantry', 'West': 'Den', 'item': 'Knife'},
    'Pantry': {'South': 'Kitchen', 'item': 'Vase'}
}

# Set the starting room for the game
room = 'Den'

# Give the player an empty bag to hold items
inventory = []


def main():
    show_instructions()

    # List the available player options
    moves = ['go North', 'go South', 'go East', 'go West']

    # Add the ability to pick up each item to the moves list
    for rm in rooms.values():
        if 'item' in rm:
            moves.append('get {}'.format(rm['item']))

    # Display what is currently in the inventory and the room
    while True:
        # Set the players current location
        current_room = room
        print('You are in the', current_room)
        print('Inventory :', inventory)
        if 'item' in rooms[current_room] and rooms[current_room]['item'] not in inventory:
            print('You see a', rooms[current_room]['item'])
        # Once the room with the villain is entered, the game ends
        if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Robber':
            game_complete()
        print('----------------')
        # Ask the user for their next move
        print('Enter your move: ', end='')
        next_move = input()

        # Confirm move is valid
        if next_move not in moves:
            print('Not a valid command')
            print()

        if next_move in moves:
            # Quit and thank them for playing
            if next_move == 'exit':
                print('Thanks for playing! Hope you enjoyed the game!')
                quit()
            # Pickup item
            elif next_move.startswith('get'):
                if 'item' in rooms[current_room] and next_move == 'get ' + rooms[current_room]['item'] and rooms[current_room]['item'] not in inventory:
                    inventory.append(rooms[current_room]['item'])
                else:
                    print('Can\'t get item')
                    print()
            # Move the direction the user typed in
            else:
                direction = next_move.split()[1]
                move(direction)


# Move in the desired direction
def move(direction):
    global room
    if direction in rooms[room]:
        room = rooms[room][direction]
        # print(room, direction)
        print()
        return room
    else:
        print('Can\'t go that way')
        print()


# Show the user the instructions upon starting the game
def show_instructions():
    print('Welcome to the home defense game!')
    print('Collect 6 items to win the game, or the robber bests you in a fight.')

    # Tell the user their options within the game
    print('Move Commands: go North, go South, go East, go West')
    print('Add to Inventory: get \'item name\'')
    print('To Quit: exit')
    print()


# If the room with the villain is entered, the game ends
def game_complete():
    # If all items have been collected, the player wins
    if len(inventory) == len(rooms) - 2:
        print('Well done! You have collected all the items and thwarted the robber!')
        quit()
    # If any items are missing, the player loses
    else:
        print('Oh no! You failed to fend off the robber and your valuables have been stolen. Better luck next time.')
        print('Thanks for playing!')
        quit()


main()
