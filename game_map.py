import math
import pygame

game_map = [
    '1111111111',
    '1  1   1 1',
    '1  11 11 1',
    '1  1   1 1',
    '1      1 1',
    '1  1   1 1',
    '1  11111 1',
    '1        1',
    '1111111111'
]

color = {
    '1': (64, 64, 64),
    ' ': (153, 255, 51)
}

block_size = 40
half_block = block_size//2
player_size = 30
half_player = player_size//2
player_gap = half_block - half_player

def render(screen, player):
    for (j, line) in enumerate(game_map):
        for (i, block) in enumerate(line):
            pygame.draw.rect(screen, color[block], pygame.Rect(400 - half_block + block_size * i - int(player.x), 300 - half_block + block_size * j - int(player.y), block_size, block_size))
    #i1 = math.floor(player.x / block_size)
    #i2 = math.floor((player.x + player_size) / block_size)
    #j1 = math.floor(player.y / block_size)
    #j2 = math.floor((player.y + player_size) / block_size)
    #for (k, (i, j)) in enumerate(((i1, j1), (i1, j2), (i2, j2), (i2, j1))):
    #    pygame.draw.rect(screen, (100 + 10 * k, 0, 100 + 10 * k), pygame.Rect(400 - half_block + block_size * i - int(player.x), 300 - half_block + block_size * j - int(player.y), block_size, block_size))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(400 - half_block, 300 - half_block, player_size, player_size))

    
    

def passable(i, j):
    return game_map[j][i] == ' '

def check_collision(x, y, vx, vy):
    i1 = math.floor(x / block_size)
    i2 = math.floor((x + player_size - 1) / block_size)
    j1 = math.floor(y / block_size)
    j2 = math.floor((y + player_size - 1) / block_size)
    if not passable(i1, j1) or not passable(i1, j2):
        x = i2 * block_size
        #i1 = i2
        if vx < 0:
            vx = 0
    if not passable(i1, j2) or not passable(i2, j2):
        y = j2 * block_size - player_size
        #j2 = j1
        if vy > 0:
            vy = 0
    if not passable(i2, j2) or not passable(i2, j1):
        x = i2 * block_size - player_size
        #i2 = i1
        if vx > 0:
            vx = 0
    if not passable(i2, j1) or not passable(i1, j1):
        y = j2 * block_size
        #j1 = j2
        if vy < 0:
            vy = 0
    return x, y, vx, vy

