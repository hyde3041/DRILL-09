from pathlib import Path

from pico2d import *


CANVAS_WIDTH, CANVAS_HEIGHT = 1280, 1024
FRAME_SIZE = 100
FRAME_COUNT = 8
MOVE_SPEED = 5

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
image_dir = Path(__file__).resolve().parent
ground = load_image(str(image_dir / 'TUK_GROUND.png'))
character = load_image(str(image_dir / 'animation_sheet.png'))

running = True
character_x = CANVAS_WIDTH // 2
character_y = CANVAS_HEIGHT // 2
frame = 0
direction = 0
movement_keys = {
    SDLK_LEFT: (-1, 0),
    SDLK_RIGHT: (1, 0),
    SDLK_UP: (0, 1),
    SDLK_DOWN: (0, -1),
}


def handle_events():
    global running, direction

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                direction = 1
            elif event.key == SDLK_LEFT:
                direction = -1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP and event.key in (SDLK_LEFT, SDLK_RIGHT):
            direction = 0


while running:
    handle_events()
    clear_canvas()
    ground.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    character.clip_draw(
        frame * FRAME_SIZE,
        FRAME_SIZE,
        FRAME_SIZE,
        FRAME_SIZE,
        character_x,
        character_y,
    )
    update_canvas()
    character_x += direction * MOVE_SPEED
    frame = (frame + 1) % FRAME_COUNT
    delay(0.05)

close_canvas()

