import pygame, sys, time, random

# Inställningar
difficulty = 15 # Hastighet på konvojen
frame_size_x = 720
frame_size_y = 480

# Initiera PyGame
check_errors = pygame.init()
if check_errors[1] > 0:
    print(f'[!] Fel vid initiering: {check_errors[1]}')
    sys.exit(-1)

# Fönsterinställningar
pygame.display.set_caption('Tank Convoy - Square Operation')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Färger
asphalt = pygame.Color(50, 50, 50)     # Mörkgrå bakgrund
tank_green = pygame.Color(34, 139, 34) # Militärgrön
white = pygame.Color(255, 255, 255)
red = pygame.Color(200, 0, 0)
yellow = pygame.Color(255, 255, 0)     # Målet

fps_controller = pygame.time.Clock()

# Variabler för konvojen
# Varje del är 20x20 pixlar för att se kraftigare ut än en orm
tank_pos = [100, 60]
tank_body = [[100, 60], [80, 60], [60, 60]]

# Mål/Resurs (istället för mat)
target_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
target_spawn = True

direction = 'RIGHT'
change_to = direction
score = 0

def game_over():
    my_font = pygame.font.SysFont('impact', 70)
    game_over_surface = my_font.render('MISSION FAILED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(asphalt)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, white, 'impact', 30)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Vehicles in Convoy: ' + str(score + 3), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)

# Huvudloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

    # Logik för att förhindra att man kör rakt bakåt in i konvojen
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Flytta ledarvagnen (20 pixlar åt gången för att matcha storleken)
    if direction == 'UP':
        tank_pos[1] -= 20
    if direction == 'DOWN':
        tank_pos[1] += 20
    if direction == 'LEFT':
        tank_pos[0] -= 20
    if direction == 'RIGHT':
        tank_pos[0] += 20

    # Växande mekanism
    tank_body.insert(0, list(tank_pos))
    if tank_pos[0] == target_pos[0] and tank_pos[1] == target_pos[1]:
        score += 1
        target_spawn = False
    else:
        tank_body.pop()

    # Skapa nytt mål
    if not target_spawn:
        target_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
    target_spawn = True

    # Rita grafik
    game_window.fill(asphalt)
    
    for i, pos in enumerate(tank_body):
        # Rita varje stridsvagn i konvojen
        pygame.draw.rect(game_window, tank_green, pygame.Rect(pos[0], pos[1], 18, 18))
        # Rita en liten "lucka" eller detalj på varje vagn för mer realism
        pygame.draw.rect(game_window, asphalt, pygame.Rect(pos[0]+6, pos[1]+6, 6, 6))
        
        # Om det är ledarvagnen, rita ett litet eldrör
        if i == 0:
            if direction == 'UP': pygame.draw.rect(game_window, tank_green, pygame.Rect(pos[0]+8, pos[1]-5, 4, 10))
            if direction == 'DOWN': pygame.draw.rect(game_window, tank_green, pygame.Rect(pos[0]+8, pos[1]+15, 4, 10))
            if direction == 'LEFT': pygame.draw.rect(game_window, tank_green, pygame.Rect(pos[0]-5, pos[1]+8, 10, 4))
            if direction == 'RIGHT': pygame.draw.rect(game_window, tank_green, pygame.Rect(pos[0]+15, pos[1]+8, 10, 4))

    # Rita målet (gul markering)
    pygame.draw.rect(game_window, yellow, pygame.Rect(target_pos[0]+5, target_pos[1]+5, 10, 10))

    # Game Over-villkor
    if tank_pos[0] < 0 or tank_pos[0] > frame_size_x-20:
        game_over()
    if tank_pos[1] < 0 or tank_pos[1] > frame_size_y-20:
        game_over()
    for block in tank_body[1:]:
        if tank_pos[0] == block[0] and tank_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(difficulty)