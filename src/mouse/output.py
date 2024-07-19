from pynput import mouse
from src.camera.picture import take_picture
from src.db.methods import write_coordinates

# def on_move(x, y):
    # """Onmove handler"""
    # print(x,y)

def on_click(x, y, button, pressed):
    """Onclick handler"""
    click_stage = "Pressed" if pressed else "Released"
    print('{0} at {1}'.format(
       click_stage,
        (x, y)))
    if pressed:
        pic = take_picture()
        write_coordinates(x, y, pic)

mouse_listener = mouse.Listener(
    on_click=on_click,
    #on_move=on_move
    )
