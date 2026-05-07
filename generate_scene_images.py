import pygame
import os

pygame.init()
WIDTH, HEIGHT = 900, 650

def save_scene(name, draw_fn):
    surface = pygame.Surface((WIDTH, HEIGHT))
    draw_fn(surface)
    path = os.path.join(os.path.dirname(__file__), name)
    pygame.image.save(surface, path)
    print("Saved", path)

def draw_classroom(surface):
    surface.fill((180, 190, 210))
    pygame.draw.rect(surface, (80, 80, 80), (80, 120, 740, 360))
    pygame.draw.rect(surface, (120, 140, 170), (100, 140, 700, 320))
    for i in range(5):
        y = 170 + i * 60
        pygame.draw.rect(surface, (150, 110, 70), (120, y, 180, 40))
        pygame.draw.rect(surface, (120, 120, 120), (320, y, 180, 40))
    pygame.draw.rect(surface, (20, 60, 30), (120, 80, 240, 80))
    pygame.draw.rect(surface, (230, 230, 230), (420, 90, 360, 70))
    pygame.draw.rect(surface, (240, 240, 110), (520, 170, 120, 80))
    pygame.draw.circle(surface, (255, 255, 255), (760, 120), 40)

def draw_hallway(surface):
    surface.fill((40, 50, 60))
    for x in range(0, WIDTH, 80):
        pygame.draw.rect(surface, (80, 90, 100), (x, 0, 40, HEIGHT))
    pygame.draw.polygon(surface, (30, 30, 40), [(0, HEIGHT), (WIDTH // 2, 200), (WIDTH, HEIGHT)])
    for i in range(6):
        t = i / 6
        x = int(WIDTH * (0.25 + t * 0.5))
        pygame.draw.line(surface, (200, 200, 180), (x, HEIGHT), (x, 220 + i * 20), 4)
    pygame.draw.rect(surface, (100, 100, 110), (WIDTH - 180, 260, 120, 220))
    pygame.draw.rect(surface, (150, 150, 150), (80, 260, 120, 220))

def draw_service_corridor(surface):
    surface.fill((30, 30, 35))
    pygame.draw.rect(surface, (60, 60, 60), (0, 200, WIDTH, 240))
    for i in range(6):
        y = 220 + i * 40
        pygame.draw.line(surface, (100, 100, 110), (0, y), (WIDTH, y), 2)
    pygame.draw.rect(surface, (80, 80, 80), (100, 120, 120, 80))
    pygame.draw.rect(surface, (80, 80, 80), (680, 120, 120, 80))
    for i in range(5):
        pygame.draw.line(surface, (170, 170, 170), (150 + i * 80, 120), (150 + i * 80, 380), 8)
    pygame.draw.circle(surface, (240, 220, 150), (WIDTH - 120, 140), 30)
    pygame.draw.circle(surface, (200, 200, 220), (120, 140), 20)

def draw_staff_lounge(surface):
    surface.fill((100, 90, 80))
    pygame.draw.rect(surface, (70, 50, 40), (80, 300, 320, 180))
    pygame.draw.rect(surface, (220, 200, 170), (120, 340, 240, 120))
    pygame.draw.rect(surface, (90, 90, 90), (520, 280, 260, 220))
    pygame.draw.circle(surface, (255, 255, 255), (620, 360), 20)
    pygame.draw.rect(surface, (180, 180, 150), (560, 420, 140, 20))
    for i in range(5):
        pygame.draw.line(surface, (120, 100, 80), (100 + i * 120, 100), (100 + i * 120, 260), 12)

def draw_stairwell(surface):
    surface.fill((50, 55, 60))
    pygame.draw.rect(surface, (40, 45, 50), (80, 100, 740, 450))
    for i in range(10):
        y = 140 + i * 30
        pygame.draw.rect(surface, (100, 100, 120), (100, y, 700, 18))
    pygame.draw.line(surface, (180, 180, 180), (120, 120), (120, 560), 6)
    pygame.draw.line(surface, (180, 180, 180), (760, 120), (760, 560), 6)
    pygame.draw.rect(surface, (210, 210, 180), (360, 80, 180, 70))

def draw_office(surface):
    surface.fill((120, 130, 140))
    pygame.draw.rect(surface, (75, 75, 80), (70, 120, 320, 220))
    pygame.draw.rect(surface, (220, 220, 220), (110, 160, 240, 140))
    pygame.draw.rect(surface, (60, 60, 70), (540, 140, 260, 230))
    pygame.draw.rect(surface, (190, 180, 150), (620, 180, 80, 40))
    pygame.draw.circle(surface, (250, 250, 210), (680, 230), 24)
    pygame.draw.rect(surface, (40, 40, 50), (480, 380, 320, 40))
    pygame.draw.rect(surface, (200, 200, 220), (580, 140, 90, 30))
    pygame.draw.rect(surface, (240, 240, 200), (180, 380, 140, 20))

def draw_desk(surface):
    surface.fill((170, 175, 180))
    pygame.draw.rect(surface, (100, 80, 60), (100, 300, 700, 260))
    pygame.draw.rect(surface, (220, 220, 200), (140, 340, 620, 180))
    pygame.draw.rect(surface, (90, 90, 100), (500, 280, 220, 120))
    pygame.draw.circle(surface, (255, 255, 220), (360, 380), 36)
    pygame.draw.line(surface, (20, 20, 20), (140, 420), (760, 420), 4)

def draw_storage(surface):
    surface.fill((50, 55, 60))
    for i in range(4):
        x = 100 + i * 180
        pygame.draw.rect(surface, (90, 80, 70), (x, 220, 140, 180))
        pygame.draw.rect(surface, (120, 110, 90), (x + 20, 240, 100, 140))
    pygame.draw.rect(surface, (80, 80, 80), (80, 120, 740, 80))
    pygame.draw.rect(surface, (160, 150, 130), (520, 340, 160, 20))

def draw_office_search(surface):
    surface.fill((130, 135, 145))
    pygame.draw.rect(surface, (70, 75, 80), (100, 220, 520, 260))
    pygame.draw.rect(surface, (200, 200, 210), (140, 260, 440, 180))
    pygame.draw.rect(surface, (90, 90, 100), (700, 180, 140, 240))
    pygame.draw.circle(surface, (255, 255, 210), (440, 320), 24)

def draw_office_unlocked(surface):
    surface.fill((110, 115, 130))
    pygame.draw.rect(surface, (80, 85, 95), (80, 140, 740, 360))
    pygame.draw.line(surface, (210, 210, 190), (260, 220), (620, 220), 8)
    pygame.draw.rect(surface, (170, 170, 160), (560, 180, 160, 80))
    pygame.draw.rect(surface, (100, 100, 110), (620, 320, 120, 180))

def draw_back_alley(surface):
    surface.fill((25, 30, 40))
    pygame.draw.rect(surface, (50, 55, 65), (0, 450, WIDTH, 250))
    pygame.draw.rect(surface, (70, 75, 80), (120, 320, 140, 260))
    pygame.draw.rect(surface, (80, 90, 100), (520, 280, 180, 280))
    pygame.draw.line(surface, (160, 160, 160), (0, 450), (WIDTH, 450), 4)
    pygame.draw.circle(surface, (255, 255, 200), (760, 120), 36)

def draw_delivery_door(surface):
    surface.fill((20, 20, 30))
    pygame.draw.rect(surface, (90, 90, 100), (260, 180, 380, 420))
    pygame.draw.rect(surface, (140, 130, 120), (320, 240, 260, 320))
    pygame.draw.rect(surface, (200, 200, 220), (420, 260, 120, 200))
    pygame.draw.line(surface, (40, 40, 50), (260, 180), (640, 180), 8)

def draw_roof(surface):
    surface.fill((35, 40, 70))
    pygame.draw.rect(surface, (60, 65, 80), (80, 360, 740, 220))
    pygame.draw.rect(surface, (110, 110, 120), (340, 220, 220, 120))
    pygame.draw.line(surface, (200, 200, 220), (100, 360), (800, 360), 6)
    pygame.draw.circle(surface, (250, 250, 210), (760, 100), 30)

def draw_courtyard(surface):
    surface.fill((40, 50, 60))
    pygame.draw.rect(surface, (70, 80, 90), (0, 420, WIDTH, 230))
    pygame.draw.rect(surface, (90, 100, 110), (120, 300, 660, 120))
    pygame.draw.line(surface, (180, 180, 180), (120, 300), (780, 300), 6)
    pygame.draw.rect(surface, (200, 200, 200), (260, 200, 380, 40))

def draw_caught(surface):
    surface.fill((45, 15, 15))
    pygame.draw.rect(surface, (90, 30, 30), (80, 120, 740, 380))
    pygame.draw.line(surface, (220, 40, 40), (80, 120), (820, 500), 12)
    pygame.draw.line(surface, (220, 40, 40), (820, 120), (80, 500), 12)

def draw_escape(surface):
    surface.fill((20, 35, 50))
    for i in range(5):
        pygame.draw.line(surface, (140, 170, 210), (140 + i * 140, 0), (140 + i * 140, HEIGHT), 3)
    pygame.draw.rect(surface, (220, 220, 180), (260, 520, 380, 140))
    pygame.draw.circle(surface, (240, 240, 200), (700, 150), 44)

scenes = [
    ("classroom.jpg", draw_classroom),
    ("hallway.jpg", draw_hallway),
    ("service_corridor.jpg", draw_service_corridor),
    ("staff_lounge.jpg", draw_staff_lounge),
    ("stairwell.jpg", draw_stairwell),
    ("office.jpg", draw_office),
    ("desk.jpg", draw_desk),
    ("storage.jpg", draw_storage),
    ("office_search.jpg", draw_office_search),
    ("office_unlocked.jpg", draw_office_unlocked),
    ("back_alley.jpg", draw_back_alley),
    ("delivery_door.jpg", draw_delivery_door),
    ("roof.jpg", draw_roof),
    ("courtyard.jpg", draw_courtyard),
    ("caught.jpg", draw_caught),
    ("escape.jpg", draw_escape),
]

for filename, draw_fn in scenes:
    save_scene(filename, draw_fn)

pygame.quit()