#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show game instructions when called"""
    print('''
    RPG Game
    ========
    Commands:
      go [directions]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    #
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #
    print('Inventory:', inventory)
    #
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

inventory = []

rooms = {
        'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'west' : 'Bedroom',
                  'item' : 'key'
                },

         'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster'
                },
        'Dining Room' : {
                  'west' : 'Hall',
                  'south' : 'Garden',
                  'item' : 'potion'
                  },
            'Garden' : {
                'north' : 'Dining Room'
                },
            'Bedroom' : {
                'east' : 'Hall',
                'item' : 'jacket'
                }
        }
currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()

    move = ''
    while move =='':
        move = input('>')

        move = move.lower().split(" ", 1)

        if move[0] == 'go':

            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print('You can\'t go that way!')

    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

