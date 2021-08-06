import keyboard
import time

time.sleep(5)
for x in range(1092, 10000):
    print(x)

    time.sleep(0.15)
    keyboard.press('backspace')
    time.sleep(0.15)
    keyboard.press('backspace')
    time.sleep(0.15)
    keyboard.press('backspace')
    time.sleep(0.15)
    keyboard.press('backspace')
    if x < 10:
        time.sleep(0.1)

        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press(str(x))
        time.sleep(0.1)
        keyboard.press('enter')
        time.sleep(0.5)

    if x == 10:
        time.sleep(0.1)

        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('1')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('enter')
        time.sleep(0.5)


    if x>10 and x<100:
        time.sleep(0.1)
        number = str(x)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press(number[0])
        time.sleep(0.1)
        keyboard.press(number[1])
        time.sleep(0.1)
        keyboard.press('enter')

        time.sleep(0.5)

    if x == 100:
        time.sleep(0.1)

        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('1')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('enter')
        time.sleep(0.5)


    if x>100 and x<1000:
        time.sleep(0.1)
        number = str(x)

        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press(number[0])
        time.sleep(0.1)
        keyboard.press(number[1])
        time.sleep(0.1)
        keyboard.press(number[2])
        time.sleep(0.1)
        keyboard.press('enter')

        time.sleep(0.5)

    if x == 1000:
        time.sleep(0.1)

        keyboard.press('1')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('0')
        time.sleep(0.1)
        keyboard.press('enter')
        time.sleep(0.5)

    if x>1000 and x<10000:
        time.sleep(0.1)
        number = str(x)


        keyboard.press(number[0])
        time.sleep(0.1)
        keyboard.press(number[1])
        time.sleep(0.1)
        keyboard.press(number[2])
        time.sleep(0.1)
        keyboard.press(number[3])
        time.sleep(0.1)
        keyboard.press('enter')

        time.sleep(0.5)




