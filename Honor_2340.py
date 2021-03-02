from PIL import Image
import os
import time
import tkinter.messagebox

mNums = [255, 254, 253, 195]
x = 0


def tap_screen(x_axis, y_axis, delay):
    os.system('adb shell input tap %d %d' % (x_axis, y_axis))
    time.sleep(delay)


if __name__ == "__main__":
    while True:
        x += 1
        print(time.strftime('%H:%M:%S'), ' 第 %d 次挑战 ' % x)
        tap_screen(1700, 880, 7)

        for i in range(51):
            print("\rClick {} ".format('%02d' % i), end="")
            tap_screen(2050, 900, 0.3)

        for m in range(3):
            os.system('adb shell screencap -p ./sdcard/ss.png')
            os.system('adb pull ./sdcard/ss.png  D:/aa/ss.png')
            pixel_list = Image.open('D:/aa/ss.png').getpixel((1500, 460))

            if pixel_list[0] in mNums:
                break
            elif m != 2:
                for i in range(5):
                    tap_screen(2050, 900, 0.5)
            else:
                tkinter.messagebox.showerror('ERROR', pixel_list)

        tap_screen(1900, 1000, 0.8)
