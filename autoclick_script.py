from keyboard import is_pressed as press
import pyautogui
import random
import time

def main():
    print("Press Shift+A+(1 - 6) to select click speed)")
    print("Press Shift+A+X to exit")

    hotkey_speeds = {
        'shift+a+1': 1,
        'shift+a+2': 2,
        'shift+a+3': 3,
        'shift+a+4': 4,
        'shift+a+5': 5,
        'shift+a+6': 6,
    }

    start = False
    while start == False:
        if press('shift+a+x'):
            print("Exiting...")
            break
        
        for hotkey, speed in hotkey_speeds.items():
            if press(hotkey):
                click_speed = speed
                print(f"Click speed set to {click_speed}")
                start = True

    if click_speed == 6:
        while True:
            if press('shift+a+x'):
                print("Exiting...")
                break
            else:
                pyautogui.click()

    else:
        while True:
            time.sleep(random.uniform(0.1, 0.4) ** click_speed)

            if press('shift+a+x'):
                print("Exiting...")
                break
            else:
                pyautogui.click()
            
if __name__ == "__main__":
    main()
