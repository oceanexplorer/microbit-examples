import microbit as mb

def main():
    mb.display.show(mb.Image.TARGET)
    
    while True:
        if mb.button_a.was_pressed():
            mb.display.show(mb.Image.HAPPY)
        if mb.button_b.was_pressed():
            mb.display.show(mb.Image.SAD)

main()