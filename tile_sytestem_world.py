import pygame,sys

#game initialization
pygame.init()
display = pygame.display.set_mode((1000,1000  ),0,32)
pygame.display.set_caption('Farming sim')
clock = pygame.time.Clock()

#world
world = [
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","y","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","y","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","y","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","y","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","y","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
]

#player
p_x,p_y = 0,0

def render_world():
    for x in range(10):
        for y in range(18):
            if world[x][y] == "x":
                pygame.draw.rect(display, (0, 200, 150), pygame.Rect(y*100+ p_x, x*100+p_y, 100, 100))
            else:
                pygame.draw.rect(display, (0, 0, 150), pygame.Rect(y*100+p_x, x*100+p_y, 100, 100))
#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p_x += 5

    if keys[pygame.K_RIGHT]:
        p_x -= 5

    if keys[pygame.K_UP]:
        p_y += 5

    if keys[pygame.K_DOWN]:
        p_y -= 5
    
    #game code here
    
    display.fill((50, 125, 168))
    render_world()
    pygame.draw.rect(display, (200, 200, 150), pygame.Rect(500, 500, 100, 100))
    pygame.display.update()
    clock.tick(60)