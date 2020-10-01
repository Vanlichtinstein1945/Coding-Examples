########################################
#                                      #
#         A simple pong game           #
#                                      #
########################################


# Importations
import pygame, sys, os, random


# Program-wide variables
SCREEN_SIZE = [800, 600]
TITLE = "Simple Pong Game"
FPS = 60


class Object(pygame.sprite.Sprite):

    def __init__(self, color, x, y, width, height, display):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.starting_values = [-3, -2, -1, 1, 2, 3]
        self.x_move = random.choice(self.starting_values)
        self.y_move = random.choice(self.starting_values)
        self.color = color
        self.height = height
        self.width = width
        self.display = display
        self.score = 0
        self.bounce = 0
        
        self.moving_down = False
        self.moving_up = False
        self.rect_down = False
        self.rect_up = False

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(pygame.Color("White"))
        self.image.set_colorkey(pygame.Color("White"))

        self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, display):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.display = display

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(pygame.Color("White"))
        self.image.set_colorkey(pygame.Color("White"))

        self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.rect(self.display, pygame.Color("White"), [self.x, self.y, self.width, self.height])

# Main game class
class game:

    # Player dimesions: 10 x 100
    # Ball dimensions: 20 x 20
    # Goal height: 150
    # Arena wall thickness: 10
    # Edge of play area thickness: 5

    # Setting the basic window and global variables
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.display = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.arena_width = 10
        self.goal_width = 150
        self.PLAYING = True
        self.player_1 = Object(pygame.Color("Blue"), 15 + self.arena_width, (SCREEN_SIZE[1] / 2) - 50, 20, 100, self.display)
        self.player_2 = Object(pygame.Color("Red"), (SCREEN_SIZE[0] - self.arena_width) - 35, (SCREEN_SIZE[1] / 2) - 50, 20, 100, self.display)
        self.ball = Object(pygame.Color("Yellow"), (SCREEN_SIZE[0] / 2) - 20, (SCREEN_SIZE[1] / 2) - 20, 20, 20, self.display)
        self.top_left_wall = Wall(5, 5, self.arena_width, ((SCREEN_SIZE[1] - 10) / 2) - (self.goal_width / 2), self.display)
        self.bottom_left_wall = Wall(5, ((SCREEN_SIZE[1] - 10) / 2) + (self.goal_width / 2), self.arena_width, ((SCREEN_SIZE[1] - 10) / 2) - (self.goal_width / 2), self.display)
        self.top_right_wall = Wall((SCREEN_SIZE[0] - 5) - self.arena_width, 5, self.arena_width, (SCREEN_SIZE[1] / 2) - (self.goal_width / 2), self.display)
        self.bottom_right_wall = Wall((SCREEN_SIZE[0] - 5) - self.arena_width, (SCREEN_SIZE[1] / 2) + (self.goal_width / 2), self.arena_width, ((SCREEN_SIZE[1] - 10) / 2) - (self.goal_width / 2), self.display)
        self.top_wall = Wall(5, 5, SCREEN_SIZE[0] - 10, self.arena_width, self.display)
        self.bottom_wall = Wall(5, (SCREEN_SIZE[1] - 5) - self.arena_width, SCREEN_SIZE[0] - 10, self.arena_width, self.display)
        self.middle_divider = Wall((SCREEN_SIZE[0] / 2) - 1, 5, 2, SCREEN_SIZE[1] - 10, self.display)
        self.main()

    # Setting the main loop to keep the game playing
    def main(self):
        while self.PLAYING:
            self.check()
            self.update_player_1()
            self.update_player_2()
            self.update_ball()
            self.check_goal()
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)

    # Checking for button presses and other events
    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.PLAYING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if not self.player_1.y + self.player_1.height > SCREEN_SIZE[1] - self.arena_width - 7:
                        self.player_1.moving_down = True
                        self.player_1.rect_down = True
                elif event.key == pygame.K_w:
                    if not self.player_1.y < 7 + self.arena_width:
                        self.player_1.moving_up = True
                        self.player_1.rect_up = True
                if event.key == pygame.K_DOWN:
                    if not self.player_2.y + self.player_2.height > SCREEN_SIZE[1] - self.arena_width - 7:
                        self.player_2.moving_down = True
                        self.player_2.rect_down = True
                elif event.key == pygame.K_UP:
                    if not self.player_2.y < 7 + self.arena_width:
                        self.player_2.moving_up = True
                        self.player_2.rect_up = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player_1.moving_up = False
                    self.player_1.rect_up = False
                elif event.key == pygame.K_s:
                    self.player_1.moving_down = False
                    self.player_1.rect_down = False
                if event.key == pygame.K_UP:
                    self.player_2.moving_up = False
                    self.player_2.rect_up = False
                elif event.key == pygame.K_DOWN:
                    self.player_2.moving_down = False
                    self.player_2.rect_down = False

    def update_player_1(self):
        if self.player_1.y + self.player_1.height > SCREEN_SIZE[1] - self.arena_width - 7:
            self.player_1.moving_down = False
            self.player_1.rect_down = False

        if self.player_1.y < 7 + self.arena_width:
            self.player_1.moving_up = False
            self.player_1.rect_up = False

        if self.player_1.rect_up == True and self.player_1.rect_down == True:
            self.player_1.rect_up = False
            self.player_1.rect_down = False

        if self.player_1.moving_down == True and self.player_1.moving_up == False:
            self.player_1.rect_down = True

        if self.player_1.moving_up == True and self.player_1.moving_down == False:
            self.player_1.rect_up = True
        
        if self.player_1.rect_up == True:
            self.player_1.y -= 3
            
        elif self.player_1.rect_down == True:
            self.player_1.y += 3

        self.player_1.rect.center = self.player_1.x, self.player_1.y

    def update_player_2(self):
        if self.player_2.y + self.player_2.height > SCREEN_SIZE[1] - self.arena_width - 7:
            self.player_2.moving_down = False
            self.player_2.rect_down = False

        if self.player_2.y < 7 + self.arena_width:
            self.player_2.moving_up = False
            self.player_2.rect_up = False

        if self.player_2.rect_up == True and self.player_2.rect_down == True:
            self.player_2.rect_up = False
            self.player_2.rect_down = False

        if self.player_2.moving_down == True and self.player_2.moving_up == False:
            self.player_2.rect_down = True

        if self.player_2.moving_up == True and self.player_2.moving_down == False:
            self.player_2.rect_up = True
        
        if self.player_2.rect_up == True:
            self.player_2.y -= 3
            
        elif self.player_2.rect_down == True:
            self.player_2.y += 3

        self.player_2.rect.center = self.player_2.x, self.player_2.y

    def check_collision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col

    def update_ball(self):
        self.ball.rect.center = self.ball.x, self.ball.y

        if self.ball.y < self.top_wall.y + self.arena_width:
            self.ball.y_move *= -1
            self.ball.bounce += 1
        if self.ball.x + self.ball.width > self.top_right_wall.x and self.ball.y < (SCREEN_SIZE[1] / 2) - (self.goal_width / 2):
            self.ball.x_move *= -1
            self.ball.bounce += 1
        if self.ball.x + self.ball.width > self.bottom_right_wall.x and self.ball.y > (SCREEN_SIZE[1] / 2) + (self.goal_width / 2):
            self.ball.x_move *= -1
            self.ball.bounce += 1
        if self.ball.x < self.top_left_wall.x + self.arena_width and self.ball.y < ((SCREEN_SIZE[1] - 10) / 2) - (self.goal_width / 2):
            self.ball.x_move *= -1
            self.ball.bounce += 1
        if self.ball.x < self.bottom_left_wall.x + self.arena_width and self.ball.y > ((SCREEN_SIZE[1] - 10) / 2) + (self.goal_width / 2):
            self.ball.x_move *= -1
            self.ball.bounce += 1
        if self.ball.y + self.ball.height > self.bottom_wall.y:
            self.ball.y_move *= -1
            self.ball.bounce += 1

        if self.ball.x + self.ball.width > self.player_1.x and self.ball.x < self.player_1.x + self.player_1.width and self.ball.y + self.ball.height > self.player_1.y and self.ball.y < self.player_1.y + self.player_1.height:
            self.ball.x_move *= -1
            self.ball.bounce += 1
        if self.ball.x + self.ball.width > self.player_2.x and self.ball.x < self.player_2.x + self.player_2.width and self.ball.y + self.ball.height > self.player_2.y and self.ball.y < self.player_2.y + self.player_2.height:
            self.ball.x_move *= -1
            self.ball.bounce += 1

        if self.ball.bounce > 5:
            if self.ball.x_move > 0:
                self.ball.x_move += 1
            elif self.ball.x_move < 0:
                self.ball.x_move -= 1
            if self.ball.y_move > 0:
                self.ball.y_move += 1
            elif self.ball.y_move < 0:
                self.ball.y_move -= 1
            self.ball.bounce = 0

        self.ball.x += self.ball.x_move
        self.ball.y += self.ball.y_move

    def check_goal(self):
        if self.ball.x < 0:
            self.player_2.score += 1
            self.ball.x = (SCREEN_SIZE[0] / 2) - 20
            self.ball.y = (SCREEN_SIZE[1] / 2) - 20
            self.ball.x_move = random.randrange(-3,3)
            self.ball.y_move = random.randrange(-3,3)
        if self.ball.x > SCREEN_SIZE[0]:
            self.player_1.score += 1
            self.ball.x = (SCREEN_SIZE[0] / 2) - 20
            self.ball.y = (SCREEN_SIZE[1] / 2) - 20
            self.ball.x_move = random.randrange(-3,3)
            self.ball.y_move = random.randrange(-3,3)

    def score(self, text, x, y, color):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_object(text, largeText, color)
        TextRect.center = (x, y)
        self.display.blit(TextSurf, TextRect)

    def text_object(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    # Drawing the picture displayed to the user
    def draw(self):
        self.display.fill(pygame.Color("Black"))

        self.draw_arena()

        self.ball.draw()

        self.player_1.draw()
        self.player_2.draw()

        self.score(str(self.player_1.score), (SCREEN_SIZE[0] / 2) - 135, 70, pygame.Color("Blue"))
        self.score(str(self.player_2.score), (SCREEN_SIZE[0] / 2) + 125, 70, pygame.Color("Red"))

    # Drawing the arena that the game takes place in
    def draw_arena(self):
        self.top_wall.draw()
        self.top_right_wall.draw()
        self.top_left_wall.draw()
        self.bottom_right_wall.draw()
        self.bottom_left_wall.draw()
        self.bottom_wall.draw()
        self.middle_divider.draw()


if __name__ == "__main__":
    # Starting and ending the game
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.font.init()
    Class = game()
    pygame.quit()
    sys.exit()
