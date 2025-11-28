"""
Configurações e constantes do jogo
"""

# import json


# class ApplicationConfiguration:
#     def __init__(self, config_path: str):
#         parsedData = json.loads(config_path)
#         self.screen_height = parsedData["SCREEN_HEIGHT"]


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 20
GRAVITY = 2.5
GAME_SPEED = 15

GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100

PIPE_WIDTH = 80
PIPE_HEIGTH = 500
PIPE_GAP = 150

BG_LAYER = 0
PIPE_LAYER = 1
BIRD_LAYER = 2

# Assets paths
WING_SOUND = "assets/audio/wing.wav"
HIT_SOUND = "assets/audio/hit.wav"

BIRD_UP_SPRITE = "assets/sprites/bluebird-upflap.png"
BIRD_MID_SPRITE = "assets/sprites/bluebird-midflap.png"
BIRD_DOWN_SPRITE = "assets/sprites/bluebird-downflap.png"
PIPE_SPRITE = "assets/sprites/pipe-green.png"
GROUND_SPRITE = "assets/sprites/base.png"
BACKGROUND_SPRITE = "assets/sprites/background-day.png"
MESSAGE_SPRITE = "assets/sprites/message.png"
