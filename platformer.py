""" platformer

Assets:
    Background/Platforms - https://opengameart.org/content/2d-platformer-forest-pack
    Birds - https://opengameart.org/content/lpc-birds
    Fox - https://opengameart.org/content/animated-wild-animals
    Helicopter - https://opengameart.org/content/helicopter-2

Audio
    Birds/wind - https://opengameart.org/content/park-ambiences
    Bird caw - https://pixabay.com/sound-effects/crow1-5986/
    Scream - https://pixabay.com/sound-effects/wilhelm-1-86895/

"""

import pygame, simpleGE, random

   
class Fox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Fox_Run_Single.png")
        self.setSize(55, 40)
        self.position = (50, 400)
        self.inAir = True
            
    def process(self):
        if self.inAir:
            self.addForce(.4, 270)
        
        if self.y > 450:
            self.inAir = False
            self.y = 450
            self.dy = 0          
        
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += 5
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= 5   

        self.inAir = True
        for platform in self.scene.platforms:
            if self.collidesWith(platform):                
                if self.dy > 0:
                        self.bottom = platform.top
                        self.dy = 0
                        self.inAir = False
        
class Platform(simpleGE.Sprite):
    def __init__(self, scene, position):
        super().__init__(scene)
        self.position = (position)
        self.setImage("forest_pack_17.png")
        self.setSize(50, 50)
       
    def update(self):
        super().update()
        if self.mouseDown:
            self.position = pygame.mouse.get_pos()

class Birds(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cardinal.png")
        
#         self.images = [pygame.image.load("cardinal.png"),
#                        pygame.image.load("blackbird.png"),
#                        pygame.image.load("bluebird.png"),
#                        pygame.image.load("sparrow.png"),
#                        pygame.image.load("eagle.png"),
#                        ]
#         for i in range(0, 4):
#             self.images[i] = pygame.transform.scale(self.images[i], (80, 80))
        
        self.setSize(24, 20)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to random spot along the right edge
        self.y = random.randint(50,350)
        
        #x is right side of screen
        self.x = 650 
        
        #dx is random minSpeed to maxSpeed
        self.dx = (random.randint(self.minSpeed, self.maxSpeed)) * -1
        
    def checkBounds(self):
        if self.left < 0:
            self.reset()
            
class Helicopter(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("helicopter_1.png")
        self.reset()
        
    def reset(self):
        self.y = random.randint(80,300)
        self.x = 650
        self.dx = -15
    
    def checkBounds(self):
        if self.left < 0:
            self.reset()
        
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 30"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("arrows to move left and right. drag platforms around to carry fox")
        self.setImage("bg_forest.png")
        
        pygame.mixer.music.load("park.wav")
        pygame.mixer.music.set_volume(.9)
        pygame.mixer.music.play(-1)

        self.sndBirds = simpleGE.Sound("crow.mp3")
        self.numBirds = 5
        self.score = 0
        self.lblScore = LblScore()

        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30
        self.lblTime = LblTime()
        
        self.fox = Fox(self)
        self.heli = Helicopter(self)
        self.sndHeli = simpleGE.Sound("wilhelm.mp3")
        
        self.birds = []
        for i in range(self.numBirds):
            self.birds.append(Birds(self))

        self.platforms = [Platform(self, (610, 30)), 
                          Platform(self, (150, 470)), 
                          Platform(self, (610, 470))]
        
        self.sprites = [self.platforms, self.fox, self.birds, self.heli, self.lblScore, self.lblTime]
        
    def process(self):
        for bird in self.birds:        
            if bird.collidesWith(self.fox):
                bird.reset()
                self.sndBirds.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        for platform in self.platforms:       
            if self.heli.collidesWith(platform):
                self.heli.reset()
                self.sndHeli.play()
                platform = Platform(self, (1000, 1000))
                self.score -=5
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    