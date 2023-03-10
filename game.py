
#set up input system
#location descriptions specific to room, use list of location descs and then select the one that corresponds to the room number?
#player options: move neswud directions, access inventory, take item, use item, look around
#don't change these ones in-game
usableItems = {101:['item', 'item', 'item', 'item'],112:['item','item']}
validRooms = [4,14,24,28,104,128,204,214,221,222,223,224,225,226,227,228,234,244,304]
possInps = ["n","north","s","south","w","west","e","east","h","help","up","d","down","u","use","t","take","get yon flask","s","speak","q","quit","l","look","i","inventory"]
roomdict = {'221': 'description','222':'description'}
#these ones should change in-game, possibly we should first assign them in the function?? come back to this
startroomnum = 221


def move(dirt,roommove):
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
	newroomnum = dirtnum + roommove
	return newroomnum if newroomnum in validRooms else roommove


def useinv(roominv,invu):
	usable = ''
	for i in invu:
		if i in usableItems[roominv]:
			print(f'{invu[i][0]}')
			usable = 'yes'
			del invu[i]
			#somehow get what it does in here?
	if not usable:
		print("You didn't have anything to use here.")


def invdisp(invdi):
	for i in invdi:
		print(f'{i}: {invdi[i][1]}')


def takeitem(roomtak,roomstuff):
	if roomtak in roomstuff:
		return roomstuff[roomtak]
	else:
		return ''


def interaction(roomno):
	playinp = ''
	#roomdesc = roomdict[roomno]
	roomdesc = 'e'
	inventory = {'item': ['itemuse','itemdesc','itemgetdesc']}
	stuffinrooms = {'room': [stuff]}

	while playinp != 'q':
		playinp = (input(f"{roomdesc}\nWhat would you like to do?\n")).lower()
		if playinp not in possInps:
			print("Invalid input. Please choose a direction or action. (type 'h' to see possible actions)")
	
		match playinp:
			case 'n'|'north'|'s'|'south'|'e'|'east'|'w'|'west'|'up'|'d'|'down' :
				newroom = move(playinp[0],roomno)
				if newroom != roomno:
					roomno = newroom
				else:
					print(f'Cannot move {playinp} here.')

			case 'h' | 'help':
				print('Possible actions are: north, south, east, west, help, up, down, use, take, look, speak, inventory, quit')

			case 'u' | 'use':
				useinv(roomno,inventory)

			case 't' | 'take':
				try:
					newitem,newuse,newdesc = takeitem(roomno)
					inventory[newitem] = [newuse,newdesc]
					#delete the item from the room
				except:
					print('Could not take any items here.')
			
			case 'i' | 'inventory':
				invdisp(inventory)
			#case 'q' | 'quit':
				#quit

interaction(startroomnum)
#print(roomno)
