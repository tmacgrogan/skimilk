# # Mustafa Kaptan
# # Slideshow programi
import pygame, sys , ConfigParser
from pygame import gfxdraw

# Colors
BLACK = (0 , 0 , 0)
WHITE = (255, 255, 255)

class Image(pygame.sprite.Sprite):
    def __init__(self, filename, picture, time, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./experiments/" + filename + "/" + picture).convert()
        self.time = int(time)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width() / 2
        self.rect.centery = screen.get_height() / 2
        
def start_countdown(screen):    
    # Get screens width,height -> center
    centerX = screen.get_width() / 2
    centerY = screen.get_height() / 2
    
    # Font
    countfont = pygame.font.Font('turkish.ttf', 150)
    
    for i in range (4, 0, -1):
        screen.fill(BLACK)
        if i > 1:
			# Draw an anti-aliased circle
            pygame.gfxdraw.aacircle(screen, centerX, centerY, 150, WHITE)
            counttext = countfont.render("" + str(i - 1) , True, WHITE)
            screen.blit(counttext, (centerX - 40, centerY - 90))
        pygame.display.flip()
        pygame.time.delay(1000)

class Slideshow():
    def __init__(self, fname):
        
        # Initialize
        pygame.init()
        
        # Screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Slideshow")
        
        # Invisible mouse
        pygame.mouse.set_visible(False)

        # List of sprite images
        self.slideShow = pygame.sprite.OrderedUpdates()
        self.currentSlide = pygame.sprite.OrderedUpdates()
        
        # Get file name
        self.filename = fname
        
        self.config = ConfigParser.RawConfigParser()
        try:
            self.config.readfp(open("./experiments/" + self.filename + "/config.ini"))
        except IOError: 
            print "Error: can\'t find file or read data"
            pygame.quit()
        
        self.lineList = config.items('sequence')
        self.length = len(lineList)
        
        # Save lines to Image class and Slideshow list
        for line in self.lineList:
            slideImage = Image(filename, line[0], line[1], screen)
            self.slideShow.add(slideImage)
        
        # Use a timer to control FPS.
        self.clock = pygame.time.Clock()
        
        # Start the countdown
        start_countdown(screen)
            
    def pickSlide(index):
        sprites = self.slideShow.sprites()
        self.screen.fill(BLACK)
        self.currentSlide.empty()
        self.currentSlide.add(sprites[index % len(sprites)])
        self.currentSlide.draw(self.screen)
        
            
if __name__ == "__main__":
    main()
