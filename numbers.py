import microbit as mb
import random

def main():
    counter = 0
    mb.display.show(mb.Image.TARGET)
    
    while True:
        if mb.button_a.was_pressed():
            counter = counter + 1
            mb.display.show(counter)
        if mb.button_b.was_pressed():
            random_number = random.randint(0, 9)
            mb.display.show(random_number)

main()