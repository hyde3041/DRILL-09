from pathlib import Path

from pico2d import *


open_canvas()
image_dir = Path(__file__).resolve().parent
grass = load_image(str(image_dir / 'grass.png'))
character = load_image(str(image_dir / 'animation_sheet.png'))

running = True
character_x = 400
frame = 0
direction = 0


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
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, character_x, 90)
    update_canvas()
    character_x += direction * 5
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()

