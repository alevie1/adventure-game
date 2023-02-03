#just some descriptions of rooms for this game

#room1/field
"""You find yourself in a strange wasteland.
You can see no sky, and it's too dark to make out much.
To the east, metal shrapnel litters the ground.
To the west, you can vaguely make out a haze of light."""

#room2/escape
	#if all conditions reached
"""You pick your way over the field, your way lit by the lamp 
and your magical core guarded by the mithral"""
	#if you haven't found the armor
"""Approaching the field of torn metal, you can feel the energy
of the strange metal as if it is ripping you apart. You back up. Best not to go there yet."""
	#if you haven't found the light
"""It's too dark to see anything."""

#room3/travel
"""The path is worn and cracked, but was once expertly paved.
Absently, you wonder what could have damaged it so badly."""

#room4/scraps
"""A field of random junk. The items that most attract your interest are an old box, a silver mirror,
a bag filled with strange coins, and an ornate table."""
	#items - flavor text
	#mirror
		"""Looking at the tarnished metal, you can see your own distorted reflection.
		You seem to be a robot- a warforged, you recall the name to your surprise. It's odd. 
		It doesn't feel... right. You weren't always a robot, were you? Come to think of it,
		you don't really know anything about yourself at all. Strange."""
	#table
		"""Beautifully carved from cherry wood. Probably worth a lot before it was tossed here.
		Now it's filled with termites."""
	#coins
		"""Electrum pieces. You can barely make out the inscription on the face. 'inscription lol' """
	#box
		"""You open the box and pull out a shimmering silk cloak, miraculously intact.
		As you hold it, you notice your hands seem distorted behind it- hard to focus on somehow,
		like it's hiding them not from sight, but from thought."""


#room5/townsquare
"""A huge square opening near the entrance to an abandoned city. Gorgeous but decrepit buildings line the paths.
An eerie silence fills the whole place. You can't shake the feeling that you shouldn't be here. 
The streets sprawl out in front of you."""

#room6/towers
"""This road is lined with huge spires. They may have once been beautiful.
One of them seems intact enough to enter."""

#room7/labfloor1
"""A laboratory building, or perhaps a mechanic's shop? Tools line the walls and are scattered across the floor.
There's a flight of stairs at the back."""

#room8/labfloor2
"""Papers litter the floor. There's a table in the middle which holds dismembered parts, presumably of another warforged.
A notebook sits next to the scattered screws and plates."""
	#notebook
	"""Scattered notes, entries from random dates. Read them?"""
	#yes
		"""Entry no. 1: It's hard work here. Sometimes I wonder if all this 'progress' is worth it.
		Is the name of science really worth the things we've done? Another soul lost today, and no closer to perfecting the process."""
			#keep reading?

		"""Entry no. 450: We're making progress, at last. Today, we managed to transfer a single soul, subject 47, into a crystal,
		using the precise rituals we've devised. We believe this to be a breakthrough. """

		"""Entry no. 451: Subject 47 became dangerous and was terminated immediately, as per standard protocol. The ritual must be altered."""
			#keep reading?

		"""Entry no. 1096: Today, the first of the crystal-beings awakened at last. We've been calling them 'warforged' although
		their technical name is ''. The crystal seems to allow the soul inside full control over the mechanical body.
		No adverse effects so far. Could this be the secret to immortality?"""
			#keep reading?

		"""Entry no. 1549: Should we be allowed immortality? The impact of all the things I've done weighs on me more each day.
		The warforged grow ever more advanced, our successes ever more marvelous. The failures, though, grow ever more devastating.
		All these experiments in the name of progress... I fear that this will be our downfall."""
			#keep reading?

		"""Entry no. 1550: This will be the last entry I write, I fear. The council suspects a revolt, and if they find my involvement
		with the resistance efforts here, 
