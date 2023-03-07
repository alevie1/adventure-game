
#set up all vars- input, inventory, game over flag
inventory = []
playerinput = ''
gameover = 0
roomnum = 1
locations = [['description','options'],['description','optioins']]


#set up input system
#location descriptions specific to room, use list of location descs and then select the one that corresponds to the room number?
#player options: move neswud directions, access inventory, take item, use item, look at item
usableItems = {"roomno":['item', 'item', 'item', 'item'],"roomno1":['item','item']}
validRooms = [100,101,2,0,11]
possInps = ["n","north","s","south","w","west","e","east","h","help","up","d","down","u","use","g","get","get yon flask","s","speak","q","quit","l","look","i","inventory"]


def move(dirt,roomnum):
	match dirt:
		case 'n':
			dirtnum = 10
		case 's':
			dirtnum = -10
		case 'e':
			dirtnum = 1
		case 'w':
			dirtnum = -1
		case 'u':
			 dirtnum = 100
		case 'd':
 			dirtnum = -100
	newroomnum = dirtnum + roomnum
	if newroomnum in validRooms:
		return newroomnum
	else:
		return roomnum

def useinv(roomno,inventory):
	usable = ''
	for i in inventory:
		if i in usableItems[roomno]:
			usable = 'yes'
			#somehow get what it does in here?
	if usable:
		#action
		pass
	else:
		print("You didn't have anything to use here")

def interaction(roomno,inventory):
	playinp = ''
	#roomdesc = roomdict[roomno]
	roomdesc = 'e'

	while playinp != 'q':
		playinp = (input(f"{roomdesc}\nWhat would you like to do?")).lower()
		if playinp not in possInps:
			print("Invalid input. Please choose a direction or action. (type 'h' to see possible actions)")
	
		match playinp:
			case 'n'|'north'|'s'|'south'|'e'|'east'|'w'|'west'|'up'|'d'|'down' :
				newroom = move(playinp[0],roomno)
				if newroom != roomno:
					roomno = newroom
				else:
					print('Cannot move {playinp} here.')
			case 'h' | 'help':
				print('Possible actions are: north, south, west, east, help, up, down, use, get, look, speak, quit, inventory')
			case 'u' | 'use':
				useinv(roomno,inventory)
			#case 'q' | 'quit':
				#quit

	#print(roomno)

#interaction(roomnum,inventory)