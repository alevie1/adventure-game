#just some descriptions of rooms for this game

#room1/field
"""You find yourself in a strange wasteland.
You can see no sky, and it's too dark to make out much.
To the east, metal shrapnel litters the ground.
To the west, you can vaguely make out a haze of light."""

#room2/escape
	#if all conditions reached
"""You pick your way over the field, your way lit by the lamp 
and your magical core guarded by the adamantine armor."""
	#if you haven't found the armor
"""Approaching the field of torn metal, you can feel the energy
of the strange metal as if it is ripping your very soul apart. You back up. Best not to go there yet."""
	#if you haven't found the (light maybe?? unsure. other condition)
"""It's too dark to see anything."""

#room3/travel
"""The path is worn and cracked, but was once expertly paved.
Absently, you wonder what could have damaged it so badly."""

#room4/scraps
"""A field of random junk. The items that most interest you are an old box, a silver mirror,
a bag filled with strange coins, and an ornate table."""
	#items - flavor text
	#mirror
		"""Looking at the tarnished metal, you can see your own distorted reflection.
		You seem to be a robot- a warforged, you recall the name to your surprise. It's odd. 
		It doesn't feel... right. You weren't always a robot, were you? Come to think of it,
		you don't really know anything about yourself at all. Strange."""
	#table
		"""Beautifully carved from a wood-like substance. Probably worth a lot before it was tossed here.
		Now it's filled with termites."""
	#coins
		"""Electrum pieces. You can't make out the inscription on the face."""
	#box
		"""You open the box and pull out a shimmering silk cloak, miraculously intact.
		As you hold it, you notice your hands seem distorted behind it- hard to focus on somehow,
		like it's hiding them not from sight, but from thought."""


#room5/townsquare
"""A huge square opening near the entrance to an abandoned city. Gorgeous but decrepit buildings line the paths.
Strange magical phenomena are visible all around- a pillar of purple flame, a group of skittering rats with
gossamer wings, a strange shadowy figure which you think it best not to approach.
An eerie silence fills the whole place. The streets sprawl out in front of you."""

#room6/towers
"""This road is lined with huge spire-like structures. They may have once been beautiful.
One of them seems intact enough to enter."""

#room7/labfloor1
"""A laboratory building, or perhaps a mechanic's shop? Tools line the 
walls and are scattered across the floor. There's a flight of stairs at the back."""

#room8/labfloor2
"""Papers litter the floor. There's a table in the middle which holds dismembered 
parts, presumably of another warforged. A notebook sits next to the scattered screws and plates."""
	#notebook
	"""Notes and lab entries from random dates. Read them?"""
	#yes
		"""Entry no. 20: It's hard work here. Sometimes I wonder if all this 'progress' is worth it.
		Is the name of science really worth the things we've done? Another soul lost today, and no closer to perfecting the process."""
			#keep reading?

		"""Entry no. 139: The secret, it seems, lies in the crystals from the dead god's body. If the soul magic can be properly
		channelled, we could make something of it."""
			#keep reading?

		"""Entry no. 450: We're making progress, at last. Today, we managed to transfer a single soul, Subject 47, into a crystal,
		using the precise rituals we've devised. We believe this to be a breakthrough."""
			#keep reading?

		"""Entry no. 451: Subject 47 became dangerous and was terminated immediately, as per standard protocol. The ritual must be altered."""
			#keep reading?

		"""Entry no. 1096: Today, the first of the crystal-beings awakened at last. We've begun to call them 'warforged'. A bloody name,
		but I fear it will prove all too accurate. The crystal seems to allow the soul inside full control over the mechanical body.
		No adverse effects so far. Could this be the secret to immortality?"""
			#keep reading?

		"""Entry no. 1549: Should we even be allowed immortality? The impact of all the things I've done weighs on me more each day.
		The warforged grow ever more advanced, our successes ever more marvelous. The failures, though, grow ever more devastating.
		All these experiments in the name of progress... I fear that this will be our downfall."""
			#keep reading?

		"""Entry no. 1550: This will be the last entry I write, I fear. The council suspects a revolt, and if they discover my recent
		involvement with the resistance efforts here, my work could be in danger. There's a drow city a couple days to the north.
		Perhaps I can find refuge there."""
			#keep reading?
		"""The rest of the book is blank."""
		"""Under the notebook is a scrap of paper with a code written on it: [code lol]."""

#labbasement
"""A robot like you sits in the corner, mostly dismantled. Its eyes glow as it wakes up. You hear a voice in your head."""
	#robot lines
		"""Hello. It's been awhile since - - -an --yone came down here. I am - --- E -- Es Ther - -- """
		"""I h-- --- -- hav --e something yo- u are lll---l-looking for"""
		"""If youc can hel-p me f--f-fix my body. W-w-w-What do you say? Is it a- --D-eAl?"""
	#if they talk to it, it offers them a crystal in exchange for helping to rebuild its body
	#if they agree - crystal1
	#Esther can later be found standing in the second floor, busily working on something. She'll talk to you but not much.
		"""You helped Esther to put her body back together. She leaves, setting something on the floor."""
		"""A crystal. It glows blue. Holding it, you remember something..."""

#room9/mindflayers
"""It seems a group of illithids have set up a base in this part of town. You try to get past, 
but they sense your consciousness and drive you away."""

#room10/armory
"""An armory, filled with weapons and armor. Most of it is rusted beyond repair, but you catch a gleam
of metal near the back."""
	#armor
	"""It's a suit of mithral armor. You think it might be able to protect your magical essence."""
	#if they try to take more stuff - crystal5
	"""You notice a small door behind the racks. You open it. Inside is a blue crystal."""
	#if they take it
	"""A crystal. It glows blue. Holding it, you remember something..."""


#room11/crater
"""An enormous crater."""

#room12
"""There's a metal door built into the ground. Looks like you need a password to enter."""

#room13
"""Looks like the interior of a fallout bunker. Evidently it didn't protect its inhabitants well enough-
a skeleton lies in the corner. Shelves line the back wall- historical records, it appears."""
	#The records have things in them
	#If you try to take something
	"""Something glints blue from the skeleton's hand."""

#catacombs under lab
	"""As you descend deeper into the basement, into the very bowels of the city, you can feel a presence.
	Something is wrong here. At last, you reach flat ground in a tunnel. You catch a glimpse of something
	glowing ahead."""

#tomb
	"""A huge cavern. In the center lies a massive body, made of a stone-like substance. Dried oil-like
	blood cakes the ground beneath it, and huge sections are missing or collapsed. The inside is filled
	with blue crystals, which it appears were being mined from the body. You can feel one calling to you."""


#memories
#1
	"""You remember your name. Or at least, you think it was yours. Rowena. You can hear the deep voice
	saying it, and know it was someone important. Someone you loved."""
#this one is only for the tomb
	"""You remember this place. This... figure. It was once a god. A keeper of justice. You remember the
	day you first entered one of its temples, and you remember the day that your people clawed their way
	to its home plane. You remember the feeling as ichor spilled onto the ground. The feeling that nothing
	would ever be right again."""
#2
	"""You remember becoming a warforged. The soul magic was painful, but you knew you could now live forever.
	You were grateful for the immortality at the time- who knew what awaited in the afterlife after the god's death?"""
#3
	"""You remember a dwarven man, with a deep voice, whom you loved more than anything. His name was Hector. You remember
	watching him grow old, seeing his eyes as the life faded from them, because even the hundreds of years dwarves
	live are nothing next to the solitary, eternal existence of a warforged."""
#4
	"""You remember entering stasis after a catastrophic event, after your city had collapsed on itself.
	You remember intending to awaken only when you were needed. Clearly, that time is now."""
#this one activates after all 5 crystals have been found
	"""Finally, you remember everything. Your life, the day the revolts happened- the people, tired of
	living under the oppressive government built on the corpse of justice, the oligarchy, ready to
	end it all if they couldn't have all the power for themselves, and you remember what you need to do.
	You remember the runes that will allow the god's restless, trapped spirit to be laid to rest at last.
	The runes that will restore balance and let all the other souls trapped within this forgotten city
	to be free. The runes inscribed on your own metal body. You know, beyond any doubt, that this is what
	you designed yourself for. To put right what was wrong at last."""
