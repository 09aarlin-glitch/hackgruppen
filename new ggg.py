from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# --- Inställningar ---
window.fps_counter.enabled = False
window.exit_button.visible = False

# Färger
dust_sand = color.rgb(194, 178, 128)
dust_wall = color.rgb(210, 180, 140)

# --- Miljö ---
Sky(texture='sky_default')
chunk_size = 50 
loaded_chunks = set()
entities_dict = {} # Vi sparar allt i en dictionary för lättare städning

def generate_chunk(cx, cz):
    x_offset = cx * chunk_size
    z_offset = cz * chunk_size
    chunk_entities = []

    # 1. Marken
    ground = Entity(model='quad', scale=chunk_size, rotation_x=90,
                  position=(x_offset, 0, z_offset), color=dust_sand, 
                  texture='white_cube', collider='box')
    chunk_entities.append(ground)

    # 2. Labyrint-väggar
    random.seed(hash((cx, cz)))
    cell_size = 5
    
    # Startposition för väggar inuti chunken
    start_x = x_offset - (chunk_size / 2)
    start_z = z_offset - (chunk_size / 2)

    for z in range(0, chunk_size, cell_size):
        for x in range(0, chunk_size, cell_size):
            # Lämna mitten av (0,0) öppen så spelaren inte fastnar vid start
            if cx == 0 and cz == 0 and abs(x-25) < 10 and abs(z-25) < 10:
                continue
                
            # Slumpa väggar
            if random.random() > 0.75:
                w = Entity(model='cube', scale=(cell_size, 8, cell_size),
                           position=(start_x + x, 4, start_z + z),
                           color=dust_wall, texture='white_cube', collider='box')
                chunk_entities.append(w)
            
    return chunk_entities

def load_chunk(cx, cz):
    if (cx, cz) in loaded_chunks: return
    entities_dict[(cx, cz)] = generate_chunk(cx, cz)
    loaded_chunks.add((cx, cz))

def unload_chunk(cx, cz):
    if (cx, cz) not in loaded_chunks: return
    for e in entities_dict[(cx, cz)]:
        destroy(e)
    del entities_dict[(cx, cz)]
    loaded_chunks.remove((cx, cz))

# --- Spelare & Kontroller ---
# Vi startar spelaren lite högre upp (y=2) för att undvika att fastna i golvet
player = FirstPersonController(
    model='cube', 
    z=0, 
    y=2, 
    origin_y=-.5, 
    speed=12,
    mouse_sensitivity=40 # Ändrat från Vec2 till ett vanligt nummer
)

# Vapen
gun = Entity(parent=camera.ui, model='cube', color=color.dark_gray, 
             scale=(0.2, 0.1, 0.6), position=(0.5, -0.4, 0.5), rotation=(5, -5, 0))

def input(key):
    if key == 'left mouse down':
        # Skjut-effekt
        bullet = Entity(model='sphere', color=color.orange, scale=0.1, 
                        position=player.position + Vec3(0,1.5,0) + camera.forward,
                        collider='sphere')
        bullet.animate_position(bullet.position + camera.forward * 50, duration=0.4)
        destroy(bullet, delay=0.4)
    
    if key == 'escape':
        quit()

def update():
    # Chunk-logik
    cx = int(round(player.x / chunk_size))
    cz = int(round(player.z / chunk_size))

    for dx in range(-1, 2):
        for dz in range(-1, 2):
            load_chunk(cx + dx, cz + dz)

    # Avlastning
    to_unload = [c for c in loaded_chunks if abs(c[0]-cx) > 2 or abs(c[1]-cz) > 2]
    for c in to_unload:
        unload_chunk(c[0], c[1])

app.run()
