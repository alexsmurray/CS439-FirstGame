# Game overview  
  In this platformer, the player must help a fox catch birds in the woods. The play must drag movable platforms to lift the fox in conjunction with
  moving the fox left and right with arrow keys to catch birds within the time limit. 
  Be careful though, because this region is also a known fly zone for helicopters which spell bad news for the fox and platforms.
# List of assets  
  Fox  
  Platforms  
  Birds  
  Helicopters  
  Scoreboard  
  Timer  
  Game 
  ## Sprite details 
   Key attributes of every sprite:
  ### Visual elements  
  Fox - will look like a fox  
  Platforms - will look like the ground or rocks  
  Birds - Any simple bird will do, ideally would be a variety of birds for better visual appeal (not implemented)  
  Helicopter - will be a helicopter  
  Scoreboard -  a humble rectangle that shows the current score. likely with a dark background and light text to make it easily readable  
  Timer - similar to the scoreboard but displays the current time ticking down
  Game - will need a background image that depicts the woods
  ### Animation details  
  Fox - uses a sprite sheet that was provided (not implemented)  
  Birds - uses a sprite sheet that was provided (not implemented)  
  Helicopter - uses a sprite sheet that was provided (not implemented)  
  ### Life span 
  Fox - is created when game starts, does not die but can be reset when colliding with the helicopter (not implemented)  
  Platforms - created on start, there are three that can be destroyed when colliding with the helicopter (not implemented)  
  Birds - created on start, a set number of them spawn that are reset whenever they collide with the fox or reach the edge of the screen  
  Helicopter - created on start, resets when reaches the edge of the screen or colliding with the fox/platforms, should spawn at various intervals and not constantly (not implemented)  
  ### Movement 
  Fox - moves left or right using the left and right arrow keys  
  Platforms - can be dragged around using the mouse  
  Birds - move automatically from the right side of the screen to the left  
  Helicopter - moves automatically from the right side of the screen to the left
  ### Boundary behavior 
  Fox - should stop when reaching reaching the screen boundaries (only works with bottom at the moment)  
  Platforms - should stop when reaching reaching the screen boundaries (only works with bottom at the moment)  
  Birds - "disappears" off the left screen boundary but are reset back to the right side  
  Helicopter - "disappears" off the left screen boundary but are reset back to the right side
  ### Collision behavior 
  Fox - lands on the top of the platforms during collision  
  Birds - colliding with the fox adds to the score and resets the bird and sound plays  
  Helicopter - colliding with the platform removes the platform from game (not implemented) and decreases score, colliding with the fox resets it (not implemented), any collision resets the helicopter and plays sound
# GUI labels 
  Scoreboard - placed at the top of the screen out of the way of the user. displays the current score and is updated when a bird is caught by the fox or the helicopter collides with platform/fox  
  Timer - placed at the top of the screen in conjunction with the scoreboard. displays the current time left in the game until it reaches zero and ends the game
# Game class initialization
  ## Appearance 
  Game scene has a background image that shows some trees or woodline
  ## Sprites  
  All sprites for this game are created when the game starts
  ## GUI elements 
  All GUI elements for this game are created when the game starts
  ## Other assets 
  A background track is played when the game starts  
  Collision sounds for the bird and helicopter are played whenever those collisions occur  
  A scoreboard gets updated when birds or helicopters have collisions  
  The Timer gets the set game time and ticks down from when the game starts and displays that information in the GUI label
# Game class behavior 
  ## Collision management  
  Whenever the birds collide with the fox the birds reset, and the score goes up  
  Whenever the helicopter collides with the fox both are reset (not implemented) and the score is reduced  
  Whenever the helicopter collides with the platforms the helicopter is reset, the score is reduced, and the platform is removed from the game (not implemented)
  ## Sound effect triggers
  A bird sound is played during bird collision  
  A scream is played when the helicopter has a collision
  ## Score and timing updates
  The timer counts down whenever the game starts
  ## GUI updates
  The scoreboard is updated on collisions  
  The timer is updated based on game time
  ## Game end or other state change conditions
  Whenever the timer reaches zero the game ends
# Asset list 
Fox - https://opengameart.org/content/animated-wild-animals  
Birds - https://opengameart.org/content/lpc-birds  (multiple birds taken from this pack but only one is currently in game)  
Platform - https://opengameart.org/content/2d-platformer-forest-pack  
Helicopter - https://opengameart.org/content/helicopter-2  
Background Image - https://opengameart.org/content/2d-platformer-forest-pack  
Background Music - https://opengameart.org/content/park-ambiences  
Bird sound - https://pixabay.com/sound-effects/crow1-5986/  
Helicopter scream - https://pixabay.com/sound-effects/wilhelm-1-86895/
# Milestones
Step 1: Get a player sprite that can move left and right on the screen  
Step 2: Create a platform that can dragged around and lets the player sprite stand on it  
Step 3: Create "good" sprites that randomly appear on one side of the screen and move arcoss to the other before resetting and reset whenever they collide with the fox  
Step 4: Create a "bad" sprite that works similarly to the good sprites  
Step 5: Add a scoreboard that can track points  
Step 6: Add a timer to give the game an end state  
Step 7: Tighten up functionality of all interactions to ensure the game works (Happy turning in here)  
Stretch Goals:  
Step 8: Add game juice to make it more appealing  
Step 9: Continue polishing game  
# Multi-state considerations 
A home screen (not implemented) displaying options to play the game, see instructions, see top scores, or exit the game  
The game screen that allows the user to experience the game  
An end game screen (not implemented) that shows the results of the game just played  
An instrucitons screen (not implemented) that explains the rules and controls of the game  
A high scores screen (not implemented) that displays the top scores of users
