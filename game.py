
#set up all vars- input, inventory, game over flag
inventory = []
playerinput = ''
gameover = 0
roomnum = 1
locations = [['description','options'],['description','optioins']]

#set up input system
#location descriptions specific to room, use list of location descs and then select the one that corresponds to the room number?
#player options: move neswud directions, access inventory, take item, use item, look at item
while (playerinput != 'q') and (gameover != 4):
	locationdesc,options = locations[roomnum]

	playerinput = input(f'{locationdesc}\nOptions:\n' + f'{options}\n')
