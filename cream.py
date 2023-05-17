import pygame


pygame.init

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH *0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('RUN')

# framerate
clock = pygame.time.Clock()
FPS = 60

#player action
moving_left = False
moving_right = False


#colors
BG = (14,201,120)

def draw_bg():
    screen.fill(BG)




class Soldier(pygame.sprite.Sprite):
    def __init__(self,char_type ,x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        temp_list =[]

        for x in range(10):
            img = pygame.image.load(f"img/{self.char_type}/idle/{x}.png")
            img = pygame.transform.scale(img, (int(img.get_width())*scale, int(img.get_height())*scale))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        temp_list = []

        for x in range(11):
            img = pygame.image.load(f"img/{self.char_type}/run/{x}.png")
            img = pygame.transform.scale(img, (int(img.get_width())*scale, int(img.get_height())*scale))
            temp_list.append(img)
            
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def move(self, moving_left, moving_right):
        # reset movement
        dx = 0
        dy = 0

        # left or right variable
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # update position
        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
		#update animation
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frame_index]
		#check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
		#if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
        
    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time == pygame.time.get_ticks()
        


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

        
player = Soldier('NinjaFrog' ,500,200,2,10)
player2 = Soldier('NinjaFrog' ,-100,500,2,10)


run = True
while run:
    

    clock.tick(FPS)

    draw_bg()

    player.update_animation()


    player.draw()
    player2.draw()
    player.move(moving_left, moving_right)
    

    #update player action
    if moving_left or moving_right:
        player.update_action(1)#1:run
    else:
        player.update_action(1)#0:idle
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # hotkeys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
             
            if event.key == pygame.K_RIGHT:
                moving_right = True
              

        # keyboard released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
               
            if event.key == pygame.K_RIGHT:
                moving_right = False
                
    pygame.display.update()

pygame.quit()