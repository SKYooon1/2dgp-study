from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 85)

delay(3)

clear_canvas()

x = 0

while (x < 800):
  clear_canvas_now()
  grass.draw_now(400, 30)
  character.draw_now(x, 85)
  x = x + 2
  delay(0.01)

delay(3)

clear_canvas()

x = 0

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 85)
    x = x + 2
    update_canvas()
    delay(0.01)
    get_events()

delay(3)

clear_canvas()

character = load_image('run_animaiton.png')

x = 0
frame = 0

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 85)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()

delay(3)

close_canvas()
