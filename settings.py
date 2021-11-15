import pygame as pg
vec = pg.math.Vector2

# define algumas cores (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (35, 0, 0)
CYAN = (0, 255, 255)

# configurações do jogo
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Strange Planet"

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Configurações do jogador
PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'player_sheet.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'rate': 250,
                     'kickback': 200,
                     'spread': 5,
                     'damage': 10,
                     'bullet_size': 'lg',
                     'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 400,
                      'bullet_lifetime': 500,
                      'rate': 900,
                      'kickback': 300,
                      'spread': 20,
                      'damage': 5,
                      'bullet_size': 'sm',
                      'bullet_count': 12}

# Configurações do alien
ALIEN_IMG = ['alien1.png','alien2.png']
ALIEN_SPEEDS = [100, 125, 150, 175]
ALIEN_HIT_RECT = pg.Rect(0, 0, 30, 30)
ALIEN_HEALTH = 80
ALIEN_DAMAGE = 10
ALIEN_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# Configurações do alien de fogo
FIRE_ALIEN_IMG = ['fireAlien1.png','fireAlien2.png']
FIRE_ALIEN_SPEEDS = [150, 175, 200, 225]
FIRE_ALIEN_HIT_RECT = pg.Rect(0, 0, 30, 30)
FIRE_ALIEN_HEALTH = 120
FIRE_ALIEN_DAMAGE = 20
FIRE_ALIEN_KNOCKBACK = 30

# Configurações da lava
LAVA_DAMAGE = 0.1

# Efeitos
MUZZLE_FLASHES = ['whitePuff1.png', 'whitePuff2.png', 'whitePuff3.png', 'whitePuff4.png']
SPLAT = 'splat green.png'
FIRE_SPLAT = 'splat red.png'
FLASH_DURATION = 50
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = "light.png"

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 3
BULLET_LAYER = 4
ALIEN_LAYER = 2
FIRE_ALIEN_LAYER = 2
EFFECTS_LAYER = 5
ITEMS_LAYER = 1

# Itens
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 10
BOB_SPEED = 0.3

# Sons / Músicas
BG_MUSIC = 'brinstar.wav'
PLAYER_HIT_SOUNDS = ['pain/hit.wav']
ALIEN_CRY_SOUNDS = ['alien_cry_1.wav', 'alien_cry_2.wav']
ALIEN_HIT_SOUNDS = ['splat.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                 'shotgun': ['shotgun.wav']}
EFFECTS_SOUNDS = {'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}
GAME_OVER = 'game_over.wav'
WIN = 'victory-fanfare.wav'
NIGHT = 'kraids-hideout.wav'
INTRO = 'intro.wav'

#Hit rects
ITEM_HIT_RECT = pg.Rect(0, 0, 30, 30)
BULLET_HIT_RECT = pg.Rect(0, 0, 15, 15)